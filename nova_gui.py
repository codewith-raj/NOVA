import customtkinter as ctk

class NovaGUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("NOVA AI Dashboard")
        self._setup_ui()

    def _setup_ui(self):
        # Holographic-style UI elements
        self.voice_btn = ctk.CTkButton(self.root, text="🎤 Voice Command", command=self._listen)
        self.voice_btn.pack(pady=20)
        
    def _listen(self):
        # Trigger speech module
        pass