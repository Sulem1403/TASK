from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .import models
from .import schemas
from .import crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/posts/{tenant_id}", response_model= schemas.EngagementPostSchema)
def get_posts(tenant_id: int, db: Session = Depends(get_db)):
    posts = crud.get_posts_by_tenant(db, tenant_id)
    return posts

@app.post("/products/", response_model=schemas.EngagementPostProductSchema)
def create_product(product: schemas.EngagementPostProductSchema, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.post("/collections/", response_model=schemas.CollectionSchema)
def create_collection(collection: schemas.CollectionSchema, db: Session = Depends(get_db)):
    return crud.create_collection(db, collection)

@app.get("/top-engagement-posts/{tenant_id}", response_model= schemas.EngagementPostSchema)
def top_engagement_posts(tenant_id: int, db: Session = Depends(get_db)):
    return crud.get_top_engagement_posts(db, tenant_id)

@app.get("/top-products/{tenant_id}", response_model= schemas.EngagementPostProductSchema)
def top_viewed_products(tenant_id: int, db: Session = Depends(get_db)):
    return crud.get_top_viewed_products(db, tenant_id)
