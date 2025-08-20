import tomllib

from contextlib import asynccontextmanager
from typing import List
from models import GoogleAIStudioModel
from models import HuggingFaceModel
from config import ServerSettings
from models import ModelRegistry

import uvicorn
from fastapi import FastAPI

available_models = ["DistilBert"]
models = {}

def load_default_model():
    config = ServerSettings.llm_config
    default_model = {}
    return default_model

def load_model(model: str):
    return model

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Should start thinking about logging or something, langsmith?
    models = load_default_model()
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
    return ""

@app.post("/predict")
async def predict(x: str):
    result = models["text"](x)
    return {"result": result}


@app.get("/hello")
def hello_world():
    return {"Hello World"}
