from fastapi.responses import JSONResponse

from common_lib.exceptions import (
    AppException
)

from common_lib.error_codes import (
    ErrorCode
)


def register_exception_handlers(
    app,
    service_name
):

    @app.exception_handler(
        AppException
    )
    async def app_exception_handler(
        request,
        exc
    ):

        trace_id = getattr(
            request.state,
            "trace_id",
            "unknown"
        )

        return JSONResponse(

            status_code=exc.http_status,

            content={

                "success": False,

                "error": {

                    "code": exc.code,

                    "message": exc.message,

                    "field": exc.field,

                    "context": exc.context
                },

                "trace_id": trace_id,

                "service": service_name
            }
        )

    @app.exception_handler(
        Exception
    )
    async def generic_exception_handler(
        request,
        exc
    ):

        trace_id = getattr(
            request.state,
            "trace_id",
            "unknown"
        )

        return JSONResponse(

            status_code=500,

            content={

                "success": False,

                "error": {

                    "code":
                    ErrorCode.INTERNAL_ERROR,

                    "message":
                    str(exc)
                },

                "trace_id":
                trace_id,

                "service":
                service_name
            }
        )