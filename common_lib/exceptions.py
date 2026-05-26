class AppException(
    Exception
):

    def __init__(
        self,
        code,
        message,
        http_status,
        field=None,
        context=None
    ):

        super().__init__(
            message
        )

        self.code = code

        self.message = message

        self.http_status = http_status

        self.field = field

        self.context = context