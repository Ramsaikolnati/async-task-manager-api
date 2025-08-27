from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# Shared user properties
class UserBase(BaseModel):
    email: EmailStr


# For registering a new user
class UserCreate(UserBase):
    password: str
    username: str   # <-- Added username field


# For login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Response schema for user details
class UserRead(UserBase):
    id: int
    username: str
    is_active: bool = True
    is_admin: bool = False

    model_config = ConfigDict(from_attributes=True)


# Token response (JWT)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
