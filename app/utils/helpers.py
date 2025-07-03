from datetime import datetime
from typing import Any, Dict

def generate_timestamp() -> str:
    """Generate ISO format timestamp"""
    return datetime.now().isoformat()

def format_response(message: str, data: Any = None) -> Dict[str, Any]:
    """Format API response"""
    response = {"message": message}
    if data is not None:
        response["data"] = data
    return response

def validate_id(item_id: int) -> bool:
    """Validate if ID is positive integer"""
    return isinstance(item_id, int) and item_id > 0