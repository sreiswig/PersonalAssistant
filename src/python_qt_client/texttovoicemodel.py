import torch
from transformers import AutoProcessor, AutoModel

class TextToVoiceModel:
    def __init__(self, config):
        self.model_id = config["model"]
        self.args = config["args"]
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.processor = AutoProcessor.from_pretrained(self.model_id)
        self.model = AutoModel.from_pretrained(self.model_id)
        self.model.to(self.device)

    def run(self, input):
        input = self.processor(
            text=[input], return_tensors="pt", voice_preset=self.args
        )
        input = {key: value.to(self.device) for key, value in input.items()}
        print(f"suno bark is using {self.model.device}")
        speech_values = self.model.generate(**input, do_sample=True)
        speech_values = speech_values.cpu()
        print(speech_values)
        return speech_values
