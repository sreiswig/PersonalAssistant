from numpy._core.multiarray import dtype
import pyaudio
import numpy as np
import time


class Microphone:
    def __init__(self, config):
        self.sample_rate = config["sample_rate"]
        self.output_sample_rate = config["output_sample_rate"]
        self.channels = config["channels"]
        self.format = getattr(
            pyaudio, config["format"]
        )  # returns the pyaudio format represented as a string in the pyproject toml
        self.chunk_size = config["chunk_size"]
        self.silence_threshold = config["silence_threshold"]
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.format,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            frames_per_buffer=self.chunk_size,
        )

    def listen(self):
        frames = []
        is_speaking = False
        last_spoken_time = time.time()

        print("Speak")
        while True:
            data = self.stream.read(self.chunk_size)
            audio_data = np.frombuffer(data, dtype=np.int16)
            frames.append(audio_data)
            energy = np.sum(np.square(audio_data))

            if energy > self.silence_threshold:
                is_speaking = True
                last_spoken_time = time.time()
            elif is_speaking and energy < self.silence_threshold:
                if time.time() - last_spoken_time > 0.5:
                    break

        return np.hstack(frames)

    def speak(self, input):
        output_stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.output_sample_rate,
            output=True,
        )
        audio_data = (input.numpy() * 32767).astype(np.int16)
        output_stream.write(audio_data.tobytes())
        output_stream.stop_stream()
        output_stream.close()

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
