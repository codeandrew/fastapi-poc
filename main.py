#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request
from pydantic import BaseModel 

app = FastAPI()

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
async def read_root(request: Request):
    header = request.headers
    client = request.client.host
    body =  await request.json()

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

