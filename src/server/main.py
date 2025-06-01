import tomllib

from contextlib import asynccontextmanager
from .models import GoogleAIStudioModel
from .models import HuggingFaceModel
from .config import ServerSettings

import uvicorn
from fastapi import FastAPI

model = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    config = ServerSettings()
    # Should start thinking about logging or something

    yield
    model.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello AIServer"}


@app.post("/predict")
async def predict(x: str):
    result = model["text"](x)
    return {"result": result}
