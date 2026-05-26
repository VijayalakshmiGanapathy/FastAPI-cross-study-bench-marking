from fastapi import FastAPI

from routers import analytics

from common_lib.middleware import (
    TraceIDMiddleware
)

from common_lib.exception_handlers import (
    register_exception_handlers
)


# Create FastAPI application
app = FastAPI(
    title="Validation Analytics API",
    version="1.0.0"
)


# Add middleware
app.add_middleware(
    TraceIDMiddleware
)


# Register exception handlers
register_exception_handlers(
    app=app,
    service_name="cross-study-service"
)


# Include routers
app.include_router(
    analytics.router,
    prefix="/api/v1",
    tags=["Analytics"]
)


# Health check endpoint
@app.get("/")
def health_check():

    return {
        "message": (
            "Validation Analytics API "
            "is running successfully"
        )
    }