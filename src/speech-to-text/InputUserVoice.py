import random
import string

import openai
import wave
import sys
import pyaudio


# Class that inputs user voice
class InputUserVoice:
    def __init__(self,
                 path_to_audio_file='',
                 CHUNK=1024,
                 FORMAT=pyaudio.paInt16,
                 CHANNELS=1 if sys.platform == 'darwin' else 2,
                 RATE=44100,
                 RECORD_SECONDS=5,
                 p=pyaudio.PyAudio()
                 ):
        self.path_to_audio_file = path_to_audio_file
        self.audio_file = None
        self.transcript = ''
        self.CHUNK = CHUNK
        self.FORMAT = FORMAT
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.RECORD_SECONDS = RECORD_SECONDS
        self.p = p

    def generate_random_audio_file(self, N=7):
        new_file = 'input-wav/'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N)).join('.wav')
        self.set_path_to_audio_file(new_file)
        return new_file
    def record_audio(self, length_in_seconds=5):
        self.generate_random_audio_file()
        self.RECORD_SECONDS = length_in_seconds
        with wave.open(self.get_path_to_audio_file(), 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)

            stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True)

            print('Recording...')
            for _ in range(0, self.RATE // self.CHUNK * self.RECORD_SECONDS):
                wf.writeframes(stream.read(self.CHUNK))
            print('Done')

            stream.close()
            self.p.terminate()
    def get_output_text(self):
        if self.get_audio_file() is None:
            self.open_audio_file()
        transcript = openai.Audio.transcribe("whisper-1", self.get_audio_file())
        self.set_transcript(transcript)
        return transcript

    def get_transcript(self):
        return self.transcript
    def set_transcript(self, transcript):
        self.transcript = transcript

    def set_audio_file(self, audio_file):
        self.audio_file = audio_file
    def get_audio_file(self):
        return self.audio_file

    def open_audio_file(self, path):
        self.set_audio_file( open(self.get_path_to_audio_file(), 'rb') )
    def set_path_to_audio_file(self, file):
        self.path_to_audio_file = file
    def get_path_to_audio_file(self):
        return self.path_to_audio_file

