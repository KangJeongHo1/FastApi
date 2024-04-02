from fastapi import FastAPI
from routes.users import router as user_router

app = FastAPI()

app.include_router(user_router) # django > settings.py

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)