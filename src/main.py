import tomllib
from Microphone import Microphone
from VoiceToTextModel import VoiceToTextModel

def get_config():
    with open("pyproject.toml", "rb") as f:
        return tomllib.load(f)

def main():
    config = get_config()
    print(config["microphone"])
    m = Microphone(config["microphone"])
    v2t = VoiceToTextModel(config["voicetotext"])
    results = m.listen()
    results = v2t.run(results)
    print(results)
    m.close()

if __name__ == "__main__":
    main()
