from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ------------------------
# Book Schemas
# ------------------------
class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True  # Updated for Pydantic V2 (was orm_mode=True)


# ------------------------
# User Schemas
# ------------------------
class UserBase(BaseModel):
    name: str
    email: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# ------------------------
# Borrow Record Schema
# ------------------------
class BorrowRecord(BaseModel):
    user_id: int
    book_id: int
    borrow_date: Optional[datetime] = None  # Allow auto/default timestamp
    return_date: Optional[datetime] = None

    class Config:
        from_attributes = True


# ------------------------
# Book Recommendation Schema
# ------------------------
class BookRecommendationRequest(BaseModel):
    preference: str
