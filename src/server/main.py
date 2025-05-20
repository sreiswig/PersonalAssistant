import subprocess
import tomllib

from typing import Union
from contextlib import asynccontextmanager
from models.google_ai_studio_models import GoogleAIStudioModel
from models.huggingface_models import HuggingFaceModel

import uvicorn
from fastapi import FastAPI

model = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    config = ""
    with open("pyproject.toml", "rb") as f:
        config = tomllib.load(f)
    # Should start thinking about logging or something
    match config["distributor"]:
        case "google":
            model["text"] = GoogleAIStudioModel(config)
        case "huggingface":
            model["text"] = HuggingFaceModel(config)
        case _:
            print("default config")

    model["text"] = config["text_to_text"]
    yield
    model.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello", "AIServer"}

@app.post("/predict")
async def predict(x: str):
    result = model["text"](x)
    return {"result": result}
