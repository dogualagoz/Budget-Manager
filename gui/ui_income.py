import customtkinter as ctk

class IncomeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="💰 Gelir Ekleme Sayfası", font=("Arial", 18))
        label.pack(pady=20)