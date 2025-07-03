from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    """Base post model"""
    title: str
    content: str
    author: Optional[str] = "Anonymous"

class PostCreate(PostBase):
    """Post creation model"""
    pass

class PostUpdate(BaseModel):
    """Post update model"""
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None

class PostInDB(PostBase):
    """Post model as stored in database"""
    id: int
    created_at: str

class Post(PostInDB):
    """Post model for API responses"""
    pass

class PostsResponse(BaseModel):
    """Response model for multiple posts"""
    posts: list[Post]
    count: int