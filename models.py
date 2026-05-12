from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    DECIMAL,
    ForeignKey,
    UniqueConstraint,
    func,
)

from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


# ==================================================
# STUDIES TABLE
# ==================================================

class Study(Base):
    __tablename__ = "studies"

    study_id = Column(
        String(50),
        primary_key=True
    )

    study_title = Column(
        String(255),
        nullable=False
    )

    phase = Column(
        String(50),
        nullable=False
    )

    expected_subject_count = Column(
        Integer,
        nullable=True
    )

    status = Column(
        String(50),
        nullable=False
    )

    sdtm_version = Column(
        String(50),
        nullable=False,
        server_default="3.4"
    )

    sponsor = Column(
        String(255),
        nullable=False,
        server_default="care2data"
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    metrics = relationship(
        "ValidationMetrics",
        back_populates="study",
        cascade="all, delete-orphan"
    )


# ==================================================
# VALIDATION METRICS TABLE
# ==================================================

class ValidationMetrics(Base):
    __tablename__ = "validation_metrics"

    __table_args__ = (
        UniqueConstraint(
            "study_id",
            "run_id",
            name="uq_study_run_id"
        ),
    )

    metric_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    study_id = Column(
        String(50),
        ForeignKey("studies.study_id"),
        nullable=False,
        index=True
    )

    run_id = Column(
        String(50),
        nullable=False
    )

    calculated_at = Column(
        DateTime,
        nullable=False,
        index=True
    )

    validation_status = Column(
        String(20),
        nullable=False
    )

    status_trend = Column(
        String(20),
        nullable=True
    )

    compliance_score = Column(
        DECIMAL(5, 2),
        nullable=True
    )

    violation_score = Column(
        DECIMAL(5, 2),
        nullable=True
    )

    completeness_score = Column(
        DECIMAL(5, 2),
        nullable=True
    )

    conformance_score = Column(
        DECIMAL(5, 2),
        nullable=True
    )

    compliance_rating = Column(
        String(20),
        nullable=True
    )

    violations_count = Column(
        Integer,
        nullable=True
    )

    warnings_count = Column(
        Integer,
        nullable=True
    )

    total_violations = Column(
        Integer,
        nullable=True
    )

    total_rules = Column(
        Integer,
        nullable=True
    )

    passed_rules = Column(
        Integer,
        nullable=True
    )

    failed_rules = Column(
        Integer,
        nullable=True
    )

    records_validated = Column(
        Integer,
        nullable=True
    )

    study = relationship(
        "Study",
        back_populates="metrics"
    )