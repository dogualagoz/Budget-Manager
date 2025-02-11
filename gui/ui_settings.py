import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="⚙️ Ayarlar Sayfası", font=("Arial", 18))
        label.pack(pady=20)