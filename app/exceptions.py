"""Custom exceptions for the application"""
from fastapi import HTTPException, status


class UserNotFoundError(HTTPException):
    """Raised when a user is not found"""
    def __init__(self, email: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with email '{email}' not found"
        )


class UserAlreadyExistsError(HTTPException):
    """Raised when trying to create a user with existing email"""
    def __init__(self, email: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email '{email}' already exists"
        )


class InvalidEmailError(HTTPException):
    """Raised when email format is invalid"""
    def __init__(self, email: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid email format: '{email}'"
        )


class ValidationError(HTTPException):
    """Raised when validation fails"""
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )
