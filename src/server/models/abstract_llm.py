from abc import ABC, abstractmethod


class AbstractLLM(ABC):
    @abstractmethod
    def predict(self, text: str) -> str | None:
        pass
