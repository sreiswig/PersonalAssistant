import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class TextToTextModel:
    def __init__(self, config):
        self.model_id = config["model"]
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_id, device_map="auto")

    
    def run(self, input):
        input_ids = self.tokenizer(input, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**input_ids)
        return self.tokenizer.decode(outputs[0])