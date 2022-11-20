#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI, Request, HTTPException, File, UploadFile
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
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/upload_file")
async def upload_file(request: Request, file: UploadFile):
    if not file: return { "message": "no file sent"}

    header = request.headers
    client_ip = request.client.host

    filename = file.filename # name of the file uploaded
    contents = await file.read() # the whole file as bytes

    try:
        filename = f'uploads/{filename}'
        print(f"Saving to File: {filename}")
        
        with open (filename, 'wb') as new_file:
            new_file.write(contents)
        message = f"File {filename} Successfully Saved!"
            
    except:
        print("Can't Write file")
        message = f"File {filename} NOT saved!"

    file_object = {
        # 'file_name': contents.filename,
        "client_ip": client_ip,
        "headers": header,
        "message": message
    }
    return  file_object


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

"""
PRACTICE API
"""
@app.get("/api/family")
async def get_family(request: Request):
    hard_data = [
        {
            "name": "Andrew",
            "age": 28,
            "profile_pic": "https://avatars.githubusercontent.com/u/21142513?s=400&u=b7736e410526c452e38a9023c0239fb2eff0812a&v=4",
            "occupation": "CyberSecurity",
            "hobbies": "Playstation "
        },
        {
            "name": "Kers",
            "age": 26,
            "profile_pic": "https://scontent.fmnl6-2.fna.fbcdn.net/v/t39.30808-6/273140057_458164309294286_2244678840279332953_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=8bfeb9&_nc_eui2=AeGWjNscqCa8XzLid_TD7cboxX2cK1fyGN3FfZwrV_IY3cwp1CpSkg6D6WjD9LtMQTbmqU0MxEuoUDwLq9N0A_rH&_nc_ohc=aCH3eBx58rgAX-Cjd7y&_nc_ht=scontent.fmnl6-2.fna&oh=00_AfBNgm_3OIEWNdiu-XiMHDGZQmLokfwGMbcM_U41EFBKtQ&oe=637FC351",
            "occupation": "Front End Developer",
            "hobbies": "Food, tsaka mabadtrip "
        },
        {
            "name": "archer",
            "age": 1,
            "profile_pic":"https://scontent.fmnl6-2.fna.fbcdn.net/v/t39.30808-6/310980583_630856592025056_7532932248834882511_n.jpg?stp=cp6_dst-jpg&_nc_cat=104&ccb=1-7&_nc_sid=8bfeb9&_nc_eui2=AeGQlPFnMjnELALZqSl7j9lKAd1EOSoXDP0B3UQ5KhcM_S5IZ4lu4bu99czxM66_AD7gw3VhdjQItGktSFxMpaY8&_nc_ohc=OADw32GlrE0AX9mjrRN&_nc_ht=scontent.fmnl6-2.fna&oh=00_AfCP-PsvcuQFB2OlLd99zLxdDNEDniZUvA-GLKvhsXm9RA&oe=637EE706",
            "occupation": "Bunso",
            "hobbies": "Manira ng Tsinelas "
        },
        {
            "name": "Freya",
            "age": 1,
            "profile_pic": "https://scontent.fmnl6-1.fna.fbcdn.net/v/t39.30808-6/311313085_630856608691721_5986449925629289682_n.jpg?stp=cp6_dst-jpg&_nc_cat=101&ccb=1-7&_nc_sid=8bfeb9&_nc_eui2=AeHPTDwP1RE4to1dO-N7p9_c7WcowwG8j9_tZyjDAbyP30pVlfBSLOI0BaF6esb55_Fuw9jSoMLO_KMxneMTMLuT&_nc_ohc=kLkfqBCUH3wAX8DMXoA&_nc_ht=scontent.fmnl6-1.fna&oh=00_AfBHFy2Hkr6CBbf61t5ZFX3wY5WzN8OvQD5S4eUmIFW7ug&oe=637E1091",
            "occupation": "Ate",
            "hobbies": "Mangagaw ng upuan, Part Time Sisiw "
        }
    ]
    return hard_data