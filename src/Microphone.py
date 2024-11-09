from numpy._core.multiarray import dtype
import pyaudio
import numpy as np

class Microphone:
    def __init__(self, config):
        self.sample_rate = config["sample_rate"]
        self.channels = config["channels"]
        self.format = getattr(pyaudio, config["format"]) # returns the pyaudio format represented as a string in the pyproject toml
        self.chunk_size = config["chunk_size"]
        self.silence_threshold = config["silence_threshold"]
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format = self.format,
                                  channels = self.channels,
                                  rate = self.sample_rate,
                                  input = True,
                                  frames_per_buffer = self.chunk_size)

    def listen(self):
        frames = []
        is_speaking = False
        
        print("Speak")
        while True:
            data = self.stream.read(self.chunk_size)
            frames.append(data)

            audio_data = np.frombuffer(data, dtype=np.int16)
            energy = np.sum(np.square(audio_data))

            if energy > self.silence_threshold:
                is_speaking = True
            elif is_speaking and energy < self.silence_threshold:
                break

        return b''.join(frames)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
