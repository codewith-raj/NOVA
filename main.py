from modules.speech import NovaSpeech
from modules.ai import NovaAI
from modules.vision import NovaVision

class Nova:
    def __init__(self):
        self.speech = NovaSpeech()
        self.ai = NovaAI()
        self.vision = NovaVision()

    def run(self):
        print("⚡ NOVA AI activated. Waiting for command...")
        while True:
            command = self.speech.listen()
            if "nova" in command.lower():
                response = self.ai.respond(command)
                self.speech.speak(response)

if __name__ == "__main__":
    nova = Nova()
    nova.run()