import tomllib
from microphone import Microphone
from voice_to_text_model import VoiceToTextModel 
from text_to_voice_model import TextToVoiceModel

def get_config():
    with open("pyproject.toml", "rb") as f:
        return tomllib.load(f)

def main():
    config = get_config()
    print(config["microphone"])
    m = Microphone(config["microphone"])
    v2t = VoiceToTextModel(config["voicetotext"])
    # Setup connection to the server
    t2v = TextToVoiceModel(config["texttovoice"])
    while True:
        results = m.listen()
        results = v2t.run(results)
        print(results)
        if results["text"].strip().lower() == "stop listening.":
            break
        # Call the server and wait for results
        results = t2v.run(results)
        m.speak(results)
    m.close()

if __name__ == "__main__":
    main()
