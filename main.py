from fastapi import FastAPI
from routes import base

app = FastAPI()

app.include_router(base.router)


@app.get("/")
def index():
    return {"response":"Hello World"}

@app.get("/home")
def home():
    return{"response":"You are home"}