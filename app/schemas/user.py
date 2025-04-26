from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="The length of the name field must be more than 3 characters and less than or equal to 20 characters.",
    )
    email: EmailStr = Field(..., description="Must be correct Email format.")


class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
