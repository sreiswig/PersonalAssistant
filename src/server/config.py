from pydantic_settings import BaseSettings, SettingsConfigDict
import os
class LLMConfig(BaseSettings):
    """LLM model Config"""
    model_name: str = "distilbert/distilbert-base-uncased"
    quantization: bool = False
    device: str = "cpu"

def get_llm_config() -> LLMConfig:
    return LLMConfig()
