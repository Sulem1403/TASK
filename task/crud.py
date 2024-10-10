from sqlalchemy.orm import Session
from . import models, schemas

def get_posts_by_tenant(db: Session, tenant_id: int):
    return db.query(models.EngagementPost).filter(models.EngagementPost.tenant_id == tenant_id).all()

def create_product(db: Session, product: schemas.EngagementPostProductSchema):
    db_product = models.EngagementPostProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_collection(db: Session, collection: schemas.CollectionSchema):
    db_collection = models.Collection(**collection.dict())
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection

def get_top_engagement_posts(db: Session, tenant_id: int):
    return db.query(models.EngagementPost).filter(models.EngagementPost.tenant_id == tenant_id).order_by(models.EngagementPost.id.desc()).limit(5).all()

def get_top_viewed_products(db: Session, tenant_id: int):
    return db.query(models.EngagementPostProduct).join(models.EngagementPostProductMapping).join(models.EngagementPost).filter(
        models.EngagementPost.tenant_id == tenant_id).order_by(models.EngagementPostProductMapping.id.desc()).limit(5).all()
