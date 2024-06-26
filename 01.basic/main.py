from fastapi import FastAPI
from items import router as items_router
from users import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)

# route
@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}") # /items/1?name=jeongho
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    # ASGI 서버
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level='debug', reload=True)