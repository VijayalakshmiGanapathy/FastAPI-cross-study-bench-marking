from pydantic import BaseModel
from typing import List, Optional, Dict, Literal
from datetime import datetime


# ----------------------------
# ENUM VALIDATION
# ----------------------------

StudyStatus = Literal[
    "Active", 
    "Completed", 
    "Draft"
]

PhaseType = Literal[
    "Phase I",
    "Phase II",
    "Phase III"
]

ValidationStatus = Literal[
    "PASSED",
    "WARNINGS",
    "CRITICAL"
]

StatusTrend = Literal[
    "improving",
    "worsening",
    "stable"
]

ComplianceRating = Literal[
    "EXCELLENT",
    "GOOD",
    "FAIR",
    "POOR",
    "CRITICAL"
]


# ----------------------------
# Run History
# ----------------------------

class RunHistoryItem(BaseModel):
    run_id: str
    calculated_at: datetime

    compliance_score: float
    violations_count: int

    validation_status: ValidationStatus


# ----------------------------
# Study Response
# ----------------------------

class StudyItem(BaseModel):
    study_id: str
    study_title: str

    phase: PhaseType
    status: StudyStatus

    expected_subject_count: int
    sdtm_version: str
    #sponsor: Optional[str] = None
    latest_run_id: str
    latest_calculated_at: datetime

    total_runs: int

    compliance_score: float
    violation_score: float
    completeness_score: float
    conformance_score: float

    compliance_rating: ComplianceRating
    validation_status: ValidationStatus
    status_trend: Optional[StatusTrend]

    violations_count: int
    warnings_count: int

    vs_benchmark: Optional[float] = None
    vs_benchmark_label: Optional[str] = None

    run_history: Optional[List[RunHistoryItem]] = []


# ----------------------------
# Final API Response
# ----------------------------

class CrossStudyResponse(BaseModel):
    generated_at: str

    phase_filter: Optional[str]

    phase_benchmarks: Dict[str, float]

    studies: List[StudyItem]