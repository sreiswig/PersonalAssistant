from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from abstractllm import AbstractLLM


class HuggingFaceModel:
    def __init__(self, config):
        self.model_id = config.model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id, device_map="auto"
        )

    def run(self, input):
        input_ids = self.tokenizer(input, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**input_ids)
        return self.tokenizer.decode(outputs[0])
