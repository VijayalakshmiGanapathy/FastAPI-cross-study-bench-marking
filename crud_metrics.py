from sqlalchemy.orm import Session
from sqlalchemy import func

from typing import List, Optional

from models import ValidationMetrics

# ==================================================
# Latest metrics for one study
# ==================================================

def get_latest_metrics_for_study(
    db: Session,
    study_id: str
) -> Optional[ValidationMetrics]:
    """
    Retrieve latest validation metrics for a study.

    Args:
    db (Session): Database session.
        study_id (str): Study identifier.

    Returns:
        Optional[ValidationMetrics]: Latest metrics row.
    """

    return (
        db.query(ValidationMetrics)
        .filter(
            ValidationMetrics.study_id == study_id
        )
        .order_by(
            ValidationMetrics.calculated_at.desc()
        )
        .first()
    )


# ==================================================
# All metrics for one study
# ==================================================

def get_all_metrics_for_study(
    db: Session,
    study_id: str
) -> List[ValidationMetrics]:
    """
    Retrieve all validation runs for a study.

    Args:
        db (Session): Database session.
        study_id (str): Study identifier.

    Returns:
        List[ValidationMetrics]: Validation history.
    """

    return (
        db.query(ValidationMetrics)
        .filter(
            ValidationMetrics.study_id == study_id
        )
        .order_by(
            ValidationMetrics.calculated_at.desc()
        )
        .all()
    )


# ==================================================
# Latest metrics for all studies
# ==================================================

def get_latest_metrics_all_studies(
    db: Session
) -> List[ValidationMetrics]:
    """
    Retrieve latest validation metrics for all studies.

    Returns:
        List[ValidationMetrics]: Latest study metrics.
    """
    subquery = (
        db.query(
            ValidationMetrics.study_id,
            func.max(
                ValidationMetrics.calculated_at
            ).label("max_date")
        )
        .group_by(
            ValidationMetrics.study_id
        )
        .subquery()
    )

    return (
        db.query(ValidationMetrics)
        .join(
            subquery,
            (
                ValidationMetrics.study_id
                == subquery.c.study_id
            )
            &
            (
                ValidationMetrics.calculated_at
                == subquery.c.max_date
            )
        )
        .all()
    )


# ==================================================
# Count validation runs
# ==================================================

def get_run_count_for_study(
    db: Session,
    study_id: str
) -> int:
    """
    Count validation runs for a study.

    Args:
        db (Session): Database session.
        study_id (str): Study identifier.

    Returns:
        int: Total run count.
    """
    return (
        db.query(
            func.count(
                ValidationMetrics.metric_id
            )
        )
        .filter(
            ValidationMetrics.study_id == study_id
        )
        .scalar()
    )
