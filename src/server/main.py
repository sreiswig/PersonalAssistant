import subprocess

from typing import Union
from contextlib import asynccontextmanager

from fastapi import FastAPI

models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    models["text"] = None
    yield
    models.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello", "AIServer"}

@app.get("/predict")
async def predict(x: float):
    result = models["text"](x)
    return {"result": result}
