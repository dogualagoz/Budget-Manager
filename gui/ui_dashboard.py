import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="📊 Dashboard Sayfası", font=("Arial", 18))
        label.pack(pady=5)