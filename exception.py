from fastapi import HTTPException


class StudyNotFoundException(HTTPException):
    """
    Custom exception raised when no studies
    are found for the requested phase.
    """

    def __init__(self, phase: str):
        super().__init__(
            status_code=404,
            detail=f"No studies found for phase '{phase}'"
        )