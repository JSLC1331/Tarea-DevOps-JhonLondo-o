
# Jhon Sebastián Londoño Cárdenas.


from typing import Union

from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()
URL = 'https://6302c686c6dda4f287bdba1c.mockapi.io/items'

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Métodos GET

@app.get("/items")
def read_root():
    response = requests.get(URL, {}, timeout=5)
    return {"items": response.json()}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Método PUT

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.put(URL+"/"+str(item_id), item.json(), headers = headers)
    return response.json()

# Método DELETE    

@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    response = requests.delete(URL+"/"+str(item_id))
    return response.json()

# Método POST

@app.post("/items")
def create_item(item: Item):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(URL, item.json(), headers = headers)
    return response.json()
