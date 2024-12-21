import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

class VoiceToTextModel:
    def __init__(self, config):
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(config["model"], torch_dtype=torch.float16, low_cpu_mem_usage=True, attn_implementation="sdpa")
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        self.processor = AutoProcessor.from_pretrained(config["model"])
        self.pipe = pipeline(
                "automatic-speech-recognition",
                model=self.model,
                tokenizer=self.processor.tokenizer,
                feature_extractor=self.processor.feature_extractor,
                chunk_length_s=30,
                batch_size=16,
                torch_dtype=torch.float16,
                device=self.device,
                )

    def run(self, audio):
        print(f"Running Voice to Text on {self.device}")
        return self.pipe(audio)
