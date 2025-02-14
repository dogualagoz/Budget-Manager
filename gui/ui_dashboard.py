import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#1e1e1e")  # Koyu tema arka plan

        #* Kontrol Paneli Başlığı
        self.header_label = ctk.CTkLabel(self, text="Kontrol Paneli", font=("Arial", 20, "bold"), text_color="white")
        self.header_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        #* Bakiye Alanı
        self.balance_label = ctk.CTkLabel(self, text="Bakiye: 5000₺", font=("Arial", 16, "bold"), text_color="white")
        self.balance_label.grid(row=0, column=1, padx=20, pady=10, sticky="e")

        #* Aylık Özet Çerçevesi
        self.summary_frame = ctk.CTkFrame(self, fg_color="#2c3e50", corner_radius=8)
        self.summary_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        self.summary_label = ctk.CTkLabel(self.summary_frame, text="Aylık Özet", font=("Arial", 14, "bold"), text_color="white")
        self.summary_label.pack(pady=10)
        
        #* Aylık Özet Grafiği
        self.create_summary_chart()
    
    def create_summary_chart(self):
        fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
        ax.set_facecolor("#2c3e50")  # Arka planı sidebar ile uyumlu yap
        ax.figure.patch.set_facecolor("#2c3e50")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        
        # Örnek veri (Günlük harcama)
        days = list(range(1, 11))
        expenses = [2, 5, 3, 7, 6, 4, 8, 5, 9, 6]
        ax.bar(days, expenses, color="#3498db")
        
        canvas = FigureCanvasTkAgg(fig, master=self.summary_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
