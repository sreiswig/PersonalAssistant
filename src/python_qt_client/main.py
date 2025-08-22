import tomllib
import torch
import argparse
from voicetotextmodel import VoiceToTextModel
from texttovoicemodel import TextToVoiceModel
from gui import App


def get_config():
    with open("pyproject.toml", "rb") as f:
        return tomllib.load(f)


def cli_arguments():
    parser = argparse.ArgumentParser(
        prog="PersonalAssistantClient",
        description="A client for my personal assistant.",
        epilog="Do great things",
    )
    parser.add_argument("-g", action="store_true")


def main():
    cli_arguments()
    config = get_config()
    voiceToText = None
    textToVoice = None
    if torch.cuda.is_available():
        voiceToText = VoiceToTextModel(config["voicetotext"])
        textToVoice = TextToVoiceModel(config["texttovoice"])
        App(config, voiceToText, textToVoice)


if __name__ == "__main__":
    main()
