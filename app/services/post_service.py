from typing import List, Optional
from app.models.post import Post, PostCreate, PostUpdate
from app.utils.database import get_data_store
from app.utils.helpers import generate_timestamp

class PostService:
    """Service for post-related operations"""
    
    @staticmethod
    def get_all_posts() -> List[Post]:
        """Get all posts"""
        data_store = get_data_store()
        return [Post(**post) for post in data_store["posts"]]
    
    @staticmethod
    def get_post_by_id(post_id: int) -> Optional[Post]:
        """Get post by ID"""
        data_store = get_data_store()
        for post_data in data_store["posts"]:
            if post_data["id"] == post_id:
                return Post(**post_data)
        return None
    
    @staticmethod
    def create_post(post_data: PostCreate) -> Post:
        """Create a new post"""
        data_store = get_data_store()
        
        new_post = Post(
            id=len(data_store["posts"]) + 1,
            title=post_data.title,
            content=post_data.content,
            author=post_data.author,
            created_at=generate_timestamp()
        )
        
        data_store["posts"].append(new_post.model_dump())
        return new_post
    
    @staticmethod
    def update_post(post_id: int, post_data: PostUpdate) -> Optional[Post]:
        """Update an existing post"""
        data_store = get_data_store()
        
        for i, post in enumerate(data_store["posts"]):
            if post["id"] == post_id:
                # Update only provided fields
                update_data = post_data.model_dump(exclude_unset=True)
                data_store["posts"][i].update(update_data)
                return Post(**data_store["posts"][i])
        return None
    
    @staticmethod
    def delete_post(post_id: int) -> bool:
        """Delete a post"""
        data_store = get_data_store()
        
        for i, post in enumerate(data_store["posts"]):
            if post["id"] == post_id:
                del data_store["posts"][i]
                return True
        return False