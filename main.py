import requests
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

app = FastAPI()


app.get("/")
def read_root():
    url = 'https://630287099eb72a839d7105f1.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int, item: Item):
    return Item.text

@app.post("/items/{item_id}")
def post_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}