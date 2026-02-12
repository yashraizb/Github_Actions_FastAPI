from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(BaseModel):
    """User data model with validation"""
    email: EmailStr = Field(..., description="Unique user email address")
    name: str = Field(..., min_length=1, max_length=100, description="User full name")
    age: int = Field(..., ge=0, le=150, description="User age")
    is_active: bool = Field(default=True, description="User active status")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "john@example.com",
                "name": "John Doe",
                "age": 30,
                "is_active": True
            }
        }


class UserCreate(BaseModel):
    """Schema for creating a new user (without id)"""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)
    is_active: bool = Field(default=True)


class UserUpdate(BaseModel):
    """Schema for updating a user (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: Optional[bool] = None
