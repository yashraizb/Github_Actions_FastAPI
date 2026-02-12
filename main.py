"""FastAPI User Management Application"""
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routes import router
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="User Management API",
    description="CRUD API for managing users with in-memory storage",
    version="1.0.0"
)

# Include routes
app.include_router(router)


# Global exception handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle validation errors"""
    logger.error(f"Validation error on {request.url}: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": "Validation failed",
            "errors": exc.errors()
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions"""
    logger.error(f"Unexpected error on {request.url}: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal server error",
            "message": "An unexpected error occurred"
        }
    )


@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint"""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "message": "API is running"}
    )


@app.get("/", tags=["root"])
def root():
    """Root endpoint"""
    return JSONResponse(
        status_code=200,
        content={
            "message": "Welcome to User Management API",
            "docs": "/docs",
            "api_version": "1.0.0"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
