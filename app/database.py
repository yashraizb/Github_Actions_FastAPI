"""User service for managing in-memory user storage"""
from typing import Dict, List, Optional
from app.models import User, UserCreate, UserUpdate


class UserService:
    """Service class for user management operations"""
    
    def __init__(self):
        """Initialize user service with empty in-memory storage"""
        self.users_db: Dict[str, User] = {}
    
    def get_all_users(self) -> List[User]:
        """Get all users"""
        return list(self.users_db.values())
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.users_db.get(email)
    
    def add_user(self, user_create: UserCreate) -> User:
        """Add a new user"""
        user = User(**user_create.model_dump())
        self.users_db[user.email] = user
        return user
    
    def update_user(self, email: str, user_update: UserUpdate) -> Optional[User]:
        """Update user by email"""
        if email not in self.users_db:
            return None
        
        existing_user = self.users_db[email]
        update_data = user_update.model_dump(exclude_unset=True)
        
        # Handle email change (moving key in dictionary)
        if "email" in update_data and update_data["email"] != email:
            new_email = update_data["email"]
            if new_email in self.users_db:
                return None  # New email already exists
            del self.users_db[email]
            updated_user = existing_user.model_copy(update={**update_data})
            self.users_db[new_email] = updated_user
            return updated_user
        
        # Regular update
        updated_user = existing_user.model_copy(update={**update_data})
        self.users_db[email] = updated_user
        return updated_user
    
    def delete_user(self, email: str) -> bool:
        """Delete user by email. Returns True if user was deleted, False if not found"""
        if email in self.users_db:
            del self.users_db[email]
            return True
        return False
    
    def user_exists(self, email: str) -> bool:
        """Check if user exists by email"""
        return email in self.users_db


# Global service instance
user_service = UserService()
