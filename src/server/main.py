import tomllib

from contextlib import asynccontextmanager
from typing import List
from .models import GoogleAIStudioModel
from .models import HuggingFaceModel
from .config import ServerSettings
from .models import ModelRegistry

import uvicorn
from fastapi import FastAPI

available_models = ["DistilBert"]
model = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = ServerSettings()
    # Should start thinking about logging or something
    model = HuggingFaceModel(config.llm_config)
    yield
    


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello AIServer"}

@app.get("/model_menu")
async def get_available_models():
    return available_models

@app.post("/predict")
async def predict(x: str):
    result = model["text"](x)
    return {"result": result}

@app.get("/hello")
def hello_world():
    return {"Hello World"}
