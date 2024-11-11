from transformers import AutoProcessor, AutoModel

class TextToVoiceModel:
    def __init__(self, config):
        self.model_id = config["model"]
        self.processor = AutoProcessor.from_pretrained(self.model_id)
        self.model = AutoModel.from_pretrained(self.model_id)
        self.model = self.model.to_bettertransformer()

    def run(self, input):
        input = self.processor(text=[input], return_tensors="pt")
        speech_values = self.model.generate(**input, do_sample=True)
        return speech_values
