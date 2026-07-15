from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

items = {1: 0, 2: 1, 3: 4}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/status")
async def status():
    return {"status": "ok"}


@app.get("/metrics")
async def metric():
    return {
        "os": "5.15.167.4-microsoft-standard-WSL2",
        "runtime": "Docker",
        "framework": "FastAPI",
        "language": "Python",
        "version": "0.1.0",
        "release": "2024-06-01",
    }


@app.get("/ping")
async def ping():
    return {"output": "pong"}


@app.get("/pong")
async def pong():
    return {"output": "ping"}


@app.get("/pong-1")
async def pong_1():
    return {"output": "ping-1"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item_quantity = items.get(item_id)
    if item_quantity is None:
        raise HTTPException(status_code=404, detail="item not found.")

    return {"item_id": item_id, "q": item_quantity}
