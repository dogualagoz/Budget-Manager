import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import get_total_income, get_total_expense, get_recent_transactions

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#1e1e1e")  # Koyu tema arka plan

        # 🟢 İçerik çerçevesini ortalamak için yapılandır
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Ana kutuyu ortalamak için
        self.pack(expand=True)

        #* Kontrol Paneli Başlığı
        self.header_label = ctk.CTkLabel(self, text="📊 Dashboard", font=("Arial", 25, "bold"), text_color="white")
        self.header_label.grid(row=0, column=0, padx=40, pady=10, sticky="w")

        #* Bakiye Alanı

        total_income = get_total_income() # toplam gelir
        total_expense = get_total_expense() # toplam gider
        current_balance = total_income - total_expense # Güncel bakiye hesaplama

        
        self.balance_frame = ctk.CTkFrame(self, fg_color="#2E5077", corner_radius=12)
        self.balance_frame.grid(row=1, column=0, columnspan=2, padx=40, pady=10, sticky="ew")

        self.balance_label = ctk.CTkLabel(self.balance_frame, text=f"💰 Güncel Bakiye: {current_balance}₺", font=("Arial", 18, "bold"), text_color="white")
        self.balance_label.pack(pady=10)
        self.update_balance()

        # 🟢 GELİR & GİDER kutularını eşit büyütmek için konfigüre ettik
        self.grid_columnconfigure(0, weight=1)  # Gelir kutusu
        self.grid_columnconfigure(1, weight=1)  # Gider kutusu
        self.grid_rowconfigure(2, weight=1)  # Satırın genişlemesini sağladık

        #* Gelir ve Gider Kutucukları (Eşit Genişleyecek)
        self.create_income_expense_boxes()

        #* Son İşlemler Alanı
        self.create_recent_transactions()

        #* Aylık Harcama Grafiği
        self.create_expense_chart()

    def create_income_expense_boxes(self):
        """📊 Gelir ve Gider Kutularını oluşturur (Eşit genişlikte)."""

        self.income_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        self.income_frame.grid(row=2, column=0, padx=(40,10), pady=10, sticky="nsew")  # Her yöne yayılmasını sağladık

        ctk.CTkLabel(self.income_frame, text="📈 Aylık Gelir", font=("Arial", 14, "bold"), text_color="green").pack(pady=5)
        ctk.CTkLabel(self.income_frame, text=f"{get_total_income()}₺", font=("Arial", 16, "bold"), text_color="green").pack()

        self.expense_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        self.expense_frame.grid(row=2, column=1, padx=(10,40), pady=10, sticky="nsew")  # Her yöne yayılmasını sağladık

        ctk.CTkLabel(self.expense_frame, text="📉 Aylık Harcama", font=("Arial", 14, "bold"), text_color="red").pack(pady=5)
        ctk.CTkLabel(self.expense_frame, text=f"{get_total_expense()}₺", font=("Arial", 16, "bold"), text_color="red").pack()
    
    def create_recent_transactions(self):
        """Son İşlemler Alanını oluşturur (Gelirler yeşil, giderler kırmızı)."""
        self.transactions_frame = ctk.CTkFrame(self, fg_color="#578FCA", corner_radius=12)
        self.transactions_frame.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")

        ctk.CTkLabel(self.transactions_frame, text="🛒 Son İşlemler", font=("Arial", 14, "bold"), text_color="white").pack(pady=5)

        transaction_frame = ctk.CTkScrollableFrame(self.transactions_frame, fg_color="#578FCA")
        transaction_frame.pack(fill="both", expand=True, padx=5, pady=5)

        transactions = get_recent_transactions(limit=15)  # 🟢 En son 15 işlemi tarihe göre çek

        for trans_type, category, amount, date in transactions:  # 🔹 Tarihi de aldık
            row = ctk.CTkFrame(transaction_frame, fg_color="#2E5077", corner_radius=4)
            row.pack(fill="x", pady=4, padx=2)

            # Kategori
            ctk.CTkLabel(row, text=category, font=("Arial", 12), text_color="white").pack(side="left", padx=5)

            # Miktar - Gelir Yeşil, Gider Kırmızı
            amount_color = "#27ae60" if trans_type == "income" else "#e74c3c"  # Yeşil (gelir) - Kırmızı (gider)
            ctk.CTkLabel(row, text=f"{amount}₺", font=("Arial", 12, "bold"), text_color=amount_color).pack(side="right", padx=5)
        
    def create_expense_chart(self):
        """Aylık Harcama Çizelgesi"""
        self.expense_chart_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        self.expense_chart_frame.grid(row=4, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")

        ctk.CTkLabel(self.expense_chart_frame, text="📊 Aylık Harcama Grafiği", 
                     font=("Arial", 14, "bold"), text_color="black").pack(pady=8)

        fig, ax = plt.subplots(figsize=(4, 2), dpi=100)
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("black")
        ax.spines["bottom"].set_color("black")
        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')

        days = list(range(1, 11))
        expenses = [400, 600, 500, 700, 450, 650, 800, 700, 600, 500]
        ax.bar(days, expenses, color="#3498db")

        canvas = FigureCanvasTkAgg(fig, master=self.expense_chart_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

    def update_balance(self):
        """Bakiye bilgisini günceller"""
        total_income = get_total_income()
        total_expense = get_total_expense()
        current_balance = total_income - total_expense

        self.balance_label.configure(text=f"💰 Güncel Bakiye: {current_balance}₺")

    def update_recent_transactions(self):
        """Son işlemler listesini yeniler."""
        for widget in self.transactions_frame.winfo_children():
            widget.destroy()  # Önce eski işlemleri temizle

        self.create_recent_transactions()  # Yeniden oluştur # Yeniden oluştur