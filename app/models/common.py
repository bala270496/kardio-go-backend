from pydantic import BaseModel

class HealthResponse(BaseModel):
    """Health check response model"""
    status: str
    timestamp: str

class MessageResponse(BaseModel):
    """Generic message response model"""
    message: str
    
class ErrorResponse(BaseModel):
    """Error response model"""
    error: str
    message: str
    status_code: int