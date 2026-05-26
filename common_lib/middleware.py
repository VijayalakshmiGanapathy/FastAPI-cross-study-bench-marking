import uuid

from starlette.middleware.base import (
    BaseHTTPMiddleware
)


class TraceIDMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        trace_id = str(
            uuid.uuid4()
        )

        request.state.trace_id = trace_id

        response = await call_next(
            request
        )

        response.headers[
            "X-Trace-ID"
        ] = trace_id

        return response