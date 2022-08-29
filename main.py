#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI, Request, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel 

# Creates FastAPI instance
app = FastAPI()


# Importing crud functions
import crud, models, schemas
from database import SessionLocal, engine

# Creates all tables
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items





"""
Root APIS for basic Examples 
"""

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root(request: Request):
    example =  {
        "Status": "Running!",
        "client_ip": request.client.host,
        "headers": request.headers

    }
    return example


@app.post("/")
async def post_root(request: Request):
    header = request.headers
    client = request.client.host
    try:
        body =  await request.json() 
    except:
        body = None

    print(header,  body)

    api =  {
        "header": header, 
        "client_ip": client,
        "body": body
    }

    return  api


@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item):
    return {
        "item_id": item_id,
        "q": q
    }

@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    return {
        "item_name": item.price,
        "q": q
    }

