from fastapi import FastAPI
from app import startApp

app : FastAPI = startApp()


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

