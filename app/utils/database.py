"""
Database utilities (in-memory storage for this example)
In production, replace with actual database connection
"""

# In-memory storage (replace with actual database in production)
_data_store = {
    "users": [],
    "posts": []
}

def get_data_store() -> dict:
    """Get the data store (replace with database connection in production)"""
    return _data_store

def reset_data_store():
    """Reset the data store (for testing purposes)"""
    global _data_store
    _data_store = {
        "users": [],
        "posts": []
    }