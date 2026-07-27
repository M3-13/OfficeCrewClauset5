from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from app.models import Category


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ClothingItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: Category
    description: str | None = Field(None, max_length=500)


class ClothingItemUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    category: Category | None = None
    description: str | None = Field(None, max_length=500)


class ClothingItemResponse(BaseModel):
    id: int
    user_id: int
    name: str
    category: Category
    description: str | None
    image_path: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


class OutfitCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    item_ids: list[int] = Field(..., min_length=1)


class OutfitUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=100)
    item_ids: list[int] | None = None


class OutfitResponse(BaseModel):
    id: int
    user_id: int
    name: str
    items: list[ClothingItemResponse] = []
    created_at: datetime

    model_config = {"from_attributes": True}
