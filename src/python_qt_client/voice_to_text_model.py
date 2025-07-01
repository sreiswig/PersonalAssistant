import torch
from transformers.pipelines import pipeline
from transformers.models.auto.processing_auto import AutoProcessor
from transformers.models.auto.modeling_auto import AutoModelForSpeechSeq2Seq

class VoiceToTextModel:
    def __init__(self, config):
        if torch.cuda.is_available():
            self.initialized = True
            self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
                config["model"],
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True,
                attn_implementation="sdpa",
            )
            self.device = "cuda:0"
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
        else:
            self.initialized = False

    def is_initialized(self) -> bool:
        return self.initialized

    def run(self, audio) -> str:
        print(f"Running Voice to Text on {self.device}")
        results = self.pipe(audio)
        if results is not None:
            try:
                text = str(results["text"])
                return text
            except Exception as e:
                return f"An error occured in the Voice to Text Pipeline {e}"
        return "The Voice to Text Pipeline Returned None"
