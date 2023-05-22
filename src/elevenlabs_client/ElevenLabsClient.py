from elevenlabs import generate, play

class ElevenLabsClient:
    def __init__(self,
                 text='',
                 voice='Bella',
                 model='eleven_monolingual_v1',
                 audio=None):
        self.text = text
        self.voice = voice
        self.model = model
        self.audio = audio
    def say(self, text):
        self.text = text
        self.audio = generate(
          text=self.text,
          voice=self.voice,
          model=self.model
        )
        play(audio=self.audio)
