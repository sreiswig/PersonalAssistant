from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
import tomllib
import os

class LLMConfig(BaseModel):
    model_name: str = "openai-community/gpt2"
    quantization: bool = False
    device: str = "cpu"

class ServerSettings(BaseSettings):
    llm_config: LLMConfig = LLMConfig()

