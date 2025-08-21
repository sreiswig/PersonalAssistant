import tomllib
import torch

from contextlib import asynccontextmanager
from typing import List
from models import GoogleAIStudioModel
from models import HuggingFaceModel
from config import ServerSettings
from models import ModelRegistry

import uvicorn
from fastapi import FastAPI

available_models = ["DistilBert"]
model_cache = {}
current_model = None

def load_model(model):
    global current_model
    current_model = model

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Should start thinking about logging or something, langsmith?
    load_model("gpt2")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello AIServer"}


@app.get("/model_menu")
async def get_available_models():
    return available_models

@app.post("/change_model")
async def change_model(model: str):
    load_model(model)
    return {"message": f"Changed to {model}"}

@app.post("/predict")
async def predict(x: str):
    result = "Not Implemented yet"
    return {"result": result}


@app.get("/hello")
def hello_world():
    return {"Hello World"}
