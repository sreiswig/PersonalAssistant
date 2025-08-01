from google import genai

from abstractllm import AbstractLLM


class GoogleAIStudioModel(AbstractLLM):
    def __init__(self, config):
        self.client = genai.Client(api_key="")
        self.model = config["model"]

    def predict(self, text: str) -> str | None:
        result = self.client.models.generate_content(model=self.model, contents=text)
        return result.text
