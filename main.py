from fastapi import FastAPI
from routers import analytics


app = FastAPI(
    title="Validation Analytics API",
    version="1.0.0"
)

# Include router
app.include_router(
    analytics.router,
    prefix="/api/v1",
    tags=["Analytics"]
)

