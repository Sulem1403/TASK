from pydantic import BaseModel
from typing import List, Optional

class EngagementPostSchema(BaseModel):
    id: int
    title: str
    description: str
    tenant_id: int

    class Config:
        orm_mode = True

class EngagementPostContentSchema(BaseModel):
    id: int
    post_id: int
    content_url: str

    class Config:
        orm_mode = True

class EngagementPostProductSchema(BaseModel):
    id: int
    product_name: str
    product_image: str
    sku: str

    class Config:
        orm_mode = True

class CollectionSchema(BaseModel):
    id: int
    collection_name: str

    class Config:
        orm_mode = True

class EngagementPostCollectionSchema(BaseModel):
    id: int
    collection_id: int
    post_id: int
    duration_in_seconds: int

    class Config:
        orm_mode = True
