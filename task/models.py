from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from .database import Base

class EngagementPost(Base):
    __tablename__ = 'engagement_post'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    tenant_id = Column(Integer)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    content = relationship("EngagementPostContent", back_populates="post")
    products = relationship("EngagementPostProductMapping", back_populates="post")

class EngagementPostContent(Base):
    __tablename__ = 'engagement_post_content'
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('engagement_post.id', ondelete='CASCADE'))
    content_url = Column(String(200))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    post = relationship("EngagementPost", back_populates="content")

class EngagementPostProduct(Base):
    __tablename__ = 'engagement_post_product'
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(200))
    product_image = Column(String(400))
    sku = Column(String(100), unique=True)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

class EngagementPostProductMapping(Base):
    __tablename__ = 'engagement_post_product_mapping'
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('engagement_post.id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey('engagement_post_product.id', ondelete='CASCADE'))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    post = relationship("EngagementPost", back_populates="products")
    product = relationship("EngagementPostProduct")

class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True, index=True)
    collection_name = Column(String(255))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

class EngagementPostCollection(Base):
    __tablename__ = 'engagement_post_collection'
    id = Column(Integer, primary_key=True, index=True)
    collection_id = Column(Integer, ForeignKey('collection.id', ondelete='CASCADE'))
    post_id = Column(Integer, ForeignKey('engagement_post.id', ondelete='CASCADE'))
    duration_in_seconds = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
