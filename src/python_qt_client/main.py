import tomllib
import argparse
from microphone import Microphone
from voice_to_text_model import VoiceToTextModel 
from text_to_voice_model import TextToVoiceModel
from gui import App

def get_config():
    with open("pyproject.toml", "rb") as f:
        return tomllib.load(f)

def cli_arguments():
    parser = argparse.ArgumentParser(
            prog="PersonalAssistantClient",
            description="The client for my personal assistant AI. Specifically not a web app",
            epilog="Do great things"
            )
    parser.add_argument('-g', action='store_true')

def main():
    cli_arguments()
    config = get_config()
    App(config)

if __name__ == "__main__":
    main()
