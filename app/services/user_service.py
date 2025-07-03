from typing import List, Optional
from app.models.user import User, UserCreate, UserUpdate
from app.utils.database import get_data_store
from app.utils.helpers import generate_timestamp

class UserService:
    """Service for user-related operations"""
    
    @staticmethod
    def get_all_users() -> List[User]:
        """Get all users"""
        data_store = get_data_store()
        return [User(**user) for user in data_store["users"]]
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Get user by ID"""
        data_store = get_data_store()
        for user_data in data_store["users"]:
            if user_data["id"] == user_id:
                return User(**user_data)
        return None
    
    @staticmethod
    def create_user(user_data: UserCreate) -> User:
        """Create a new user"""
        data_store = get_data_store()
        
        new_user = User(
            id=len(data_store["users"]) + 1,
            name=user_data.name,
            email=user_data.email,
            created_at=generate_timestamp()
        )
        
        data_store["users"].append(new_user.model_dump())
        return new_user
    
    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update an existing user"""
        data_store = get_data_store()
        
        for i, user in enumerate(data_store["users"]):
            if user["id"] == user_id:
                # Update only provided fields
                update_data = user_data.model_dump(exclude_unset=True)
                data_store["users"][i].update(update_data)
                return User(**data_store["users"][i])
        return None
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        """Delete a user"""
        data_store = get_data_store()
        
        for i, user in enumerate(data_store["users"]):
            if user["id"] == user_id:
                del data_store["users"][i]
                return True
        return False