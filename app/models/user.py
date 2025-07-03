from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    """Base user model"""
    name: str
    email: Optional[str] = ""

class UserCreate(UserBase):
    """User creation model"""
    pass

class UserUpdate(BaseModel):
    """User update model"""
    name: Optional[str] = None
    email: Optional[str] = None

class UserInDB(UserBase):
    """User model as stored in database"""
    id: int
    created_at: str

class User(UserInDB):
    """User model for API responses"""
    pass

class UsersResponse(BaseModel):
    """Response model for multiple users"""
    users: list[User]
    count: int