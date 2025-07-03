from fastapi import APIRouter
from app.models.common import HealthResponse
from app.utils.helpers import generate_timestamp

router = APIRouter()

@router.get("/", summary="Root endpoint")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "FastAPI Backend for Cloud Run",
        "version": "1.0.0",
        "timestamp": generate_timestamp(),
        "endpoints": [
            "GET /api/v1/users - Get all users",
            "POST /api/v1/users - Create user",
            "GET /api/v1/posts - Get all posts",
            "POST /api/v1/posts - Create post",
            "GET /api/v1/health - Health check",
            "GET /docs - API documentation"
        ]
    }

@router.get("/health", response_model=HealthResponse, summary="Health check")
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=generate_timestamp()
    )