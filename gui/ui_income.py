import customtkinter as ctk
import sys
import os


# Proje kök dizinine erişim sağla
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Veritabanı fonksiyonlarını import et
from database import add_income,add_expense



class IncomeExpenseFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#1e1e1e", corner_radius=10)

        # Başlık
        self.header_label = ctk.CTkLabel(self, text="Gelir & Gider Ekle", font=("Arial", 20, "bold"), text_color="white")
        self.header_label.pack(pady=15)

        # Miktar Alanı
        self.amount_label = ctk.CTkLabel(self, text="Miktar:", font=("Arial", 14), text_color="white")
        self.amount_label.pack(anchor="w", padx=20)
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Miktar girin...", width=300)
        self.amount_entry.pack(pady=5, padx=20)

        # Açıklama Alanı
        self.description_label = ctk.CTkLabel(self, text="Açıklama:", font=("Arial", 14), text_color="white")
        self.description_label.pack(anchor="w", padx=20)
        self.description_entry = ctk.CTkEntry(self, placeholder_text="Açıklama girin...", width=300)
        self.description_entry.pack(pady=5, padx=20)

        # Kategori seçimi
        self.category_label = ctk.CTkLabel(self, text="Kategori:", font=("Arial", 14), text_color="white")
        self.category_label.pack(anchor="w", padx=20)
        self.category_combobox = ctk.CTkComboBox(self, values=["Harçlık", "Alışveriş","Kira", "Fatura", "Yatırım", "Diğer"])
        self.category_combobox.pack(pady=5, padx=20)

        # Butonlar (Gelir Ekle - Yeşil, Gider Ekle - Kırmızı)
        self.button_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.button_frame.pack(pady=15)

        self.add_income_button = ctk.CTkButton(
            self.button_frame, text="Gelir Ekle", fg_color="#27ae60",
            text_color="white", hover_color="#1e8449", width=140,
            command=self.add_income_button  # Butona fonksiyonu bağladık
        )
        self.add_income_button.pack(side="left", padx=10)

        self.add_expense_button = ctk.CTkButton(
            self.button_frame, text="Gider Ekle", fg_color="#e74c3c",
            text_color="white", hover_color="#c0392b", width=140,
            command=self.add_expense_button )
        self.add_expense_button.pack(side="left", padx=10)

        self.message_label = ctk.CTkLabel(self, text="", font=("Arial",14), text_color="white",)
        self.message_label.pack(pady=10)

    def add_income_button(self):
        """Gelir ekleme butonu işlevi"""
        amount = self.amount_entry.get()
        category = self.category_combobox.get()
        description = self.description_entry.get()

        if not amount or not category:
            self.show_message("Lütfen Geçerli bir sayı girin", "red")
            return

        try:
            amount = float(amount)  # Miktarı sayıya çevir
            add_income(amount, category, description)  # Database.py içindeki fonksiyonu çağır
            self.show_message("Gelir başarıyla eklendi!","green")
            self.clear_entries()

            # 🟢 Dashboard Güncelle
            if self.master:
                self.master.show_dashboard()
                self.master.dashboard.update_recent_transactions()
        except ValueError:
            self.show_message("Lütfen geçerli bir sayı girin!","red")

    def add_expense_button(self):
        """Gider ekleme butonu işlevi"""
        amount = self.amount_entry.get()
        category = self.category_combobox.get()
        description = self.description_entry.get()

        if not amount or not category:
            self.show_message("Lütfen tüm alanları doldurun!", "red")
            return

        try:
            amount = float(amount)
            add_expense(amount, category, description)
            self.show_message("Gider başarıyla eklendi!", "green")
            self.clear_entries()

            # 🟢 Dashboard Güncelle
            if hasattr(self.master, 'dashboard'):
                self.master.dashboard.update_balance() 
                self.master.dashboard.update_recent_transactions()
        
        except ValueError:
            self.show_message("Lütfen geçerli bir sayı girin!", "red")

    def show_message(self, message, color):
        """Hata veya başarı mesajlarını gösterir"""
        self.message_label.configure(text=message, text_color=color)
    
    def clear_entries(self):
        """Giriş Alanlarını temizler"""
        self.amount_entry.delete(0,"end")
        self.description_entry.delete(0,"end")
