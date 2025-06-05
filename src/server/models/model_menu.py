from typing import List
from pydantic import BaseModel

class ModelMenu(BaseModel):
    name: List[str]
