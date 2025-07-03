from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.post import Post, PostCreate, PostUpdate, PostsResponse
from app.models.common import MessageResponse
from app.services.post_service import PostService
from app.utils.helpers import format_response, validate_id

router = APIRouter()

@router.get("/", response_model=PostsResponse, summary="Get all posts")
async def get_posts():
    """Get all posts"""
    posts = PostService.get_all_posts()
    return PostsResponse(posts=posts, count=len(posts))

@router.get("/{post_id}", response_model=Post, summary="Get post by ID")
async def get_post(post_id: int):
    """Get a specific post by ID"""
    if not validate_id(post_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid post ID"
        )
    
    post = PostService.get_post_by_id(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return post

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED, summary="Create post")
async def create_post(post: PostCreate):
    """Create a new post"""
    new_post = PostService.create_post(post)
    return format_response("Post created successfully", new_post)

@router.put("/{post_id}", response_model=dict, summary="Update post")
async def update_post(post_id: int, post: PostUpdate):
    """Update an existing post"""
    if not validate_id(post_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid post ID"
        )
    
    updated_post = PostService.update_post(post_id, post)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return format_response("Post updated successfully", updated_post)

@router.delete("/{post_id}", response_model=MessageResponse, summary="Delete post")
async def delete_post(post_id: int):
    """Delete a post"""
    if not validate_id(post_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid post ID"
        )
    
    deleted = PostService.delete_post(post_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return MessageResponse(message="Post deleted successfully")