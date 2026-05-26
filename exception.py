from common_lib.exceptions import (
    AppException
)

from common_lib.error_codes import (
    ErrorCode
)


class StudyNotFoundException(
    AppException
):

    def __init__(
        self,
        value: str
    ):

        super().__init__(

            code=ErrorCode.NOT_FOUND,

            message=(
                f"No studies found for: {value}"
            ),

            http_status=404,

            field=None,

            context=None
        )