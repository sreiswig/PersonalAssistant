import tomllib
from microphone import Microphone
from models import VoiceToTextModel, TextToTextModel, TextToVoiceModel

def get_config():
    with open("pyproject.toml", "rb") as f:
        return tomllib.load(f)

def main():
    config = get_config()
    print(config["microphone"])
    m = Microphone(config["microphone"])
    v2t = VoiceToTextModel(config["voicetotext"])
    llm = TextToTextModel(config["texttotext"])
    t2v = TextToVoiceModel(config["texttovoice"])
    results = m.listen()
    results = v2t.run(results)
    print(results)
    results = llm.run(results["text"])
    print(results)
    results = t2v.run(results)
    m.speak(results)
    m.close()

if __name__ == "__main__":
    main()
