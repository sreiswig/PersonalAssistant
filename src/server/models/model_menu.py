from typing import List
from pydantic import BaseModel

class ModelRegistry(BaseModel):
    name: List[str]
