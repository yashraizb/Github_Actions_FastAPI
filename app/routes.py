"""API routes for user management"""
from fastapi import APIRouter, status
from app.models import User, UserCreate, UserUpdate
from app.database import user_service
from app.exceptions import UserNotFoundError, UserAlreadyExistsError

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
def list_users():
    """Get all users"""
    return user_service.get_all_users()


@router.get("/{email}", response_model=User)
def get_user(email: str):
    """Get user by email"""
    user = user_service.get_user_by_email(email)
    if not user:
        raise UserNotFoundError(email)
    return user


@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate):
    """Create a new user"""
    if user_service.user_exists(user_create.email):
        raise UserAlreadyExistsError(user_create.email)
    return user_service.add_user(user_create)


@router.put("/{email}", response_model=User)
def update_user(email: str, user_update: UserUpdate):
    """Update user by email"""
    if not user_service.user_exists(email):
        raise UserNotFoundError(email)
    
    # Check if trying to change email to one that already exists
    if user_update.email and user_update.email != email:
        if user_service.user_exists(user_update.email):
            raise UserAlreadyExistsError(user_update.email)
    
    updated_user = user_service.update_user(email, user_update)
    if not updated_user:
        raise UserAlreadyExistsError(user_update.email)
    return updated_user


@router.delete("/{email}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(email: str):
    """Delete user by email"""
    if not user_service.delete_user(email):
        raise UserNotFoundError(email)
    return None