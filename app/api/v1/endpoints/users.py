from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.user import User, UserCreate, UserUpdate, UsersResponse
from app.models.common import MessageResponse
from app.services.user_service import UserService
from app.utils.helpers import format_response, validate_id

router = APIRouter()

@router.get("/", response_model=UsersResponse, summary="Get all users")
async def get_users():
    """Get all users"""
    users = UserService.get_all_users()
    return UsersResponse(users=users, count=len(users))

@router.get("/{user_id}", response_model=User, summary="Get user by ID")
async def get_user(user_id: int):
    """Get a specific user by ID"""
    if not validate_id(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID"
        )
    
    user = UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED, summary="Create user")
async def create_user(user: UserCreate):
    """Create a new user"""
    new_user = UserService.create_user(user)
    return format_response("User created successfully", new_user)

@router.put("/{user_id}", response_model=dict, summary="Update user")
async def update_user(user_id: int, user: UserUpdate):
    """Update an existing user"""
    if not validate_id(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID"
        )
    
    updated_user = UserService.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return format_response("User updated successfully", updated_user)

@router.delete("/{user_id}", response_model=MessageResponse, summary="Delete user")
async def delete_user(user_id: int):
    """Delete a user"""
    if not validate_id(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user ID"
        )
    
    deleted = UserService.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return MessageResponse(message="User deleted successfully")