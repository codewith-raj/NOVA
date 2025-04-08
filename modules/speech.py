import whisper
import pyttsx3
import numpy as np

class NovaSpeech:
    def __init__(self):
        self.model = whisper.load_model("medium")  # Use Whisper for ultra-accurate STT
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Futuristic voice

    def listen(self):
        print("🛰️ NOVA is listening...")
        audio = self._record_audio()  # Custom audio capture logic
        result = self.model.transcribe(audio)
        return result["text"]

    def speak(self, text):
        print(f"🌠 NOVA: {text}")
        self.engine.say(text)
        self.engine.runAndWait()