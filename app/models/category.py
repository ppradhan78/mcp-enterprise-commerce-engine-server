from pydantic import BaseModel, Field
from typing import Optional


class Category(BaseModel):
    category_id: Optional[int] = None
    category_name: str = Field(..., min_length=1)
    description: Optional[str] = None



class CategoryUpdate(BaseModel):
    category_name: str = Field(..., min_length=1)
    description: Optional[str] = None    