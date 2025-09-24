from fastapi import FastAPI
from models import Item


app=FastAPI()

items={}

@app.post("/item")
def create_item(item:Item):
    item_id=len(items)+1
    items[item_id]=item.dict()
    return{"message":"Item created","item_id":item_id}


@app.get("/items")
def  get_items():
    return{"items":items}


@app.put("/item/{item_id}")
def upadte_item(item_id:int,item:Item):
    if item_id not in items:
        return{"error":"Item not found"}
    items[item_id]=item.dict()
    return{"message":"Item updated","item_id":item_id}

@app.delete("/item/{item_id}")
def delete_item(item_id:int):
    if item_id not in items:    
        return items[item_id]
    del Item[item_id]
    return{"message":"Item deleted"}

