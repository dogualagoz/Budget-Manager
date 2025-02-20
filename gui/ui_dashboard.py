import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#1e1e1e")  # Koyu tema arka plan

        #* Kontrol Paneli Başlığı
        self.header_label = ctk.CTkLabel(self, text="📊 Dashboard", font=("Arial", 25, "bold"), text_color="white")
        self.header_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        #* Bakiye Alanı
        self.balance_frame = ctk.CTkFrame(self, fg_color="#2E5077", corner_radius=12)
        self.balance_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        self.balance_label = ctk.CTkLabel(self.balance_frame, text="💰 Güncel Bakiye: 7500₺", font=("Arial", 18, "bold"), text_color="white")
        self.balance_label.pack(pady=10)

        #* Gelir ve Gider Kutucukları
        self.create_income_expense_boxes()

        #* Son İşlemler Alanı
        self.create_recent_transactions()

        #* Aylık Harcama Grafiği
        self.create_expense_chart()

    def create_income_expense_boxes(self):
        """Gelir ve Gider Kutularını oluşturur."""
        self.income_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12, width=150, height=80)
        self.income_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        ctk.CTkLabel(self.income_frame, text="📈 Aylık Gelir", font=("Arial", 14, "bold"), text_color="green").pack(pady=5)
        ctk.CTkLabel(self.income_frame, text="12,000₺", font=("Arial", 16, "bold"), text_color="green").pack()

        self.expense_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12, width=150, height=80)
        self.expense_frame.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")

        ctk.CTkLabel(self.expense_frame, text="📉 Aylık Harcama", font=("Arial", 14, "bold"), text_color="red").pack(pady=5)
        ctk.CTkLabel(self.expense_frame, text="4,500₺", font=("Arial", 16, "bold"), text_color="red").pack()

    def create_recent_transactions(self):
        """Son İşlemler Alanını oluşturur."""
        self.transactions_frame = ctk.CTkFrame(self, fg_color="#578FCA", corner_radius=12)
        self.transactions_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        ctk.CTkLabel(self.transactions_frame, text="🛒 Son İşlemler", font=("Arial", 14, "bold"), text_color="white").pack(pady=5)

        # Scrollable işlem listesi
        transactions = [
            ("Elektrik faturası", "-350₺"),
            ("Su faturası", "-200₺"),
            ("Market alışverişi", "-600₺"),
            ("Maaş Yatırıldı", "+12,000₺"),
            ("Kira Ödemesi", "-3,000₺"),
            ("Telefon Faturası", "-250₺"),
        ]

        transaction_frame = ctk.CTkScrollableFrame(self.transactions_frame, fg_color="#578FCA")
        transaction_frame.pack(fill="both", expand=True, padx=5, pady=5)

        for desc, amount in transactions:
            row = ctk.CTkFrame(transaction_frame, fg_color="#2E5077", corner_radius=4)
            row.pack(fill="x", pady=4, padx=2)

            ctk.CTkLabel(row, text=desc, font=("Arial", 12), text_color="white").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=amount, font=("Arial", 12, "bold"), text_color="white").pack(side="right", padx=5)

    def create_expense_chart(self):
        """Aylık Harcama Çizelgesi"""
        self.expense_chart_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=12)
        self.expense_chart_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

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