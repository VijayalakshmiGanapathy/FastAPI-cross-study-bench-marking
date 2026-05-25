from datetime import datetime, timezone
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session, joinedload

from crud_metrics import (
    get_all_metrics_for_study,
    get_latest_metrics_all_studies,
    get_run_count_for_study,
)
from database import get_db
from exception import StudyNotFoundException
from logger_config import logger
from models import ValidationMetrics
from schemas import (
    CrossStudyResponse,
    RunHistoryItem,
    StudyItem,
)


router = APIRouter()


@router.get(
    "/metrics/cross-study",
    response_model=CrossStudyResponse
)
def get_cross_study_metrics(
    phase: Optional[str] = Query(default=None),
    status: Optional[str] = Query(default=None),
    include_history: bool = Query(default=False),
    db: Session = Depends(get_db)
):
    """
    Retrieve cross-study validation analytics.

    Args:
        phase (Optional[str]): Clinical phase filter.
        include_history (bool): Include validation history.
        db (Session): Database session.

    Returns:
        CrossStudyResponse: Analytics response.
    """

    logger.info("Fetching latest study metrics")

    latest_rows = get_latest_metrics_all_studies(db)

    if not latest_rows:
        logger.warning("No study metrics found")

        return {
            "generated_at": (
                datetime.now(timezone.utc).isoformat()
            ),
            "phase_filter": phase,
            "phase_benchmarks": {},
            "studies": []
        }

    rows = (
        db.query(ValidationMetrics)
        .options(
            joinedload(
                ValidationMetrics.study
            )
        )
        .filter(
            ValidationMetrics.metric_id.in_(
                [r.metric_id for r in latest_rows]
            )
        )
        .all()
    )

    logger.info(
            "Calculating phase benchmarks "
            "using latest study metrics"
    )

    phase_scores: Dict[str, List[float]] = {}

    for row in rows:
        score = float(row.compliance_score or 0)

        phase_scores.setdefault(
            row.study.phase,
            []
        ).append(score)

    phase_order = [
        "Phase I",
        "Phase II",
        "Phase III"
    ]

    phase_benchmarks = {
        phase_name: round(
            sum(phase_scores[phase_name])
            /
            len(phase_scores[phase_name]),
            2
        )
        for phase_name in phase_order
        if phase_name in phase_scores
    }

    if phase:

        logger.info(
                "Applying phase filter: %s",
                phase
        )
        
        rows = [
            row for row in rows
            if row.study.phase == phase
        ]

        if not rows:
            logger.error(
                "No studie found for phase: %s",
                phase
            )

            raise StudyNotFoundException(phase)
        

    if status:

        logger.info(
            "Applying status filter: %s",
             status
        )

        rows = [
            row for row in rows
            if row.study.status == status
        ]

        if not rows:

            logger.error(
                "No studies found for status: %s",
                status
            )

            raise StudyNotFoundException(
                status
            )


    studies_response = []

    for row in rows:
        study = row.study

        compliance_score = float(
            row.compliance_score or 0
        )

        benchmark = phase_benchmarks.get(
            study.phase,
            0
        )

        delta = round(
            compliance_score - benchmark,
            2
        )

        if delta > 0.5:
            label = "above"

        elif delta < -0.5:
            label = "below"

        else:
            label = "at"

        history_items = []

        if include_history:
            logger.info(
                "Fetching history for study: %s",
                study.study_id
            )

            history = get_all_metrics_for_study(
                db,
                study.study_id
            )

            history = list(reversed(history))

            for history_row in history:
                history_items.append(
                    RunHistoryItem(
                        run_id=history_row.run_id,
                        calculated_at=(
                            history_row.calculated_at
                        ),
                        compliance_score=float(
                            history_row.compliance_score or 0
                        ),
                        violations_count=(
                            history_row.violations_count or 0
                        ),
                        validation_status=(
                            history_row.validation_status
                        )
                    )
                )

        studies_response.append(
            StudyItem(
                study_id=study.study_id,
                study_title=study.study_title,
                phase=study.phase,
                status=study.status,
                expected_subject_count=(
                    study.expected_subject_count
                ),
                sdtm_version=study.sdtm_version,
                latest_run_id=row.run_id,
                latest_calculated_at=row.calculated_at,
                total_runs=get_run_count_for_study(
                    db,
                    study.study_id
                ),
                compliance_score=compliance_score,
                violation_score=float(
                    row.violation_score or 0
                ),
                completeness_score=float(
                    row.completeness_score or 0
                ),
                conformance_score=float(
                    row.conformance_score or 0
                ),
                compliance_rating=row.compliance_rating,
                validation_status=row.validation_status,
                status_trend=row.status_trend,
                violations_count=(
                    row.violations_count or 0
                ),
                warnings_count=(
                    row.warnings_count or 0
                ),
                vs_benchmark=delta,
                vs_benchmark_label=label,
                run_history=(
                    history_items
                    if include_history else []
                )
            )
        )

    studies_response.sort(
        key=lambda study: study.compliance_score,
        reverse=True
    )

    logger.info("Cross-study analytics completed")

    return {
        "generated_at": (
             datetime.now(
                timezone.utc
            ).isoformat()
        ),
        "phase_filter": phase,
        "status_filter": status,
        "phase_benchmarks": phase_benchmarks,
        "studies": studies_response
    }