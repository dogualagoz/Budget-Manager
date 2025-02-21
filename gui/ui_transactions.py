import customtkinter as ctk
import sys
import os

# Proje kök dizinine erişim sağla
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Veritabanı işlemleri
from database import get_all_income, get_all_expenses, delete_income, delete_expense

class TransactionsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#1e1e1e", corner_radius=10)

        # Başlık
        self.header_label = ctk.CTkLabel(self, text="Tüm İşlemler", font=("Arial", 20, "bold"), text_color="white")
        self.header_label.pack(pady=15)

        # Scrollable Canvas ve Frame
        self.canvas = ctk.CTkCanvas(self, bg="#1e1e1e", highlightthickness=0)
        self.scrollbar = ctk.CTkScrollbar(self, command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color="#1e1e1e")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # İşlem Listesi Güncelleme
        self.update_transaction_list()

    def update_transaction_list(self):
        """Gelir ve giderleri tarihe göre sıralayıp ekrana yazdırır."""
        # Önce tüm widgetları temizle
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Tüm işlemleri çek ve tarihe göre sırala
        transactions = []
        transactions.extend([("income", inc.id, inc.amount, inc.category, inc.description, inc.date) for inc in get_all_income()])
        transactions.extend([("expense", exp.id, exp.amount, exp.category, exp.description, exp.date) for exp in get_all_expenses()])
        
        # Tarihe göre sıralama (En yeni olan en üstte)
        transactions.sort(key=lambda x: x[5], reverse=True)  

        for trans_type, trans_id, amount, category, description, date in transactions:
            formatted_date = date.strftime("%d/%m/%Y")  # Tarihi biçimlendir

            # Satırın arkaplan rengi
            bg_color = "#159541" if trans_type == "income" else "#b94949"  # Yeşil (Gelir) - Kırmızı (Gider)
            fg_color = "#1e1e1e"  # Dış çerçeve rengi

            row_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=fg_color, corner_radius=10)
            row_frame.pack(fill="x", pady=2, padx=10)  # Yalnızca Y padding

            # **SATIRIN TAMAMI** (Sol: Bilgiler, Sağ: Butonlar)
            content_frame = ctk.CTkFrame(row_frame, fg_color=bg_color, corner_radius=10)
            content_frame.pack(fill="x", pady=1, padx=5, expand=True)

            # Sol Taraf: Kategori, Açıklama, Miktar, Tarih
            left_frame = ctk.CTkFrame(content_frame, fg_color=bg_color)
            left_frame.pack(side="left", fill="x", expand=True)

            category_label = ctk.CTkLabel(left_frame, text=category, width=120, text_color="white", fg_color=bg_color)
            category_label.pack(side="left", padx=5)

            description_label = ctk.CTkLabel(left_frame, text=description, width=200, text_color="white", fg_color=bg_color)
            description_label.pack(side="left")

            amount_label = ctk.CTkLabel(left_frame, text=f"{amount}₺", width=100, text_color="white", fg_color=bg_color)
            amount_label.pack(side="left", padx=5)

            date_label = ctk.CTkLabel(left_frame, text=formatted_date, width=100, text_color="white", fg_color=bg_color)
            date_label.pack(side="left", padx=5)

            # **Sağ Taraf: Güncelle ve Sil Butonları**
            right_frame = ctk.CTkFrame(content_frame, fg_color=bg_color)
            right_frame.pack(side="right", padx=5)

            update_button = ctk.CTkButton(right_frame, text="Güncelle", fg_color="#f39c12", text_color="white", width=70,
                                          hover_color="#d68910", command=lambda: print("Güncelleme fonksiyonu eklenecek!"))
            update_button.pack(side="left", padx=5)

            delete_button = ctk.CTkButton(right_frame, text="X",font=("Arial",14,"bold"), fg_color="#e74c3c", text_color="white", width=50,
                                          hover_color="#c0392b", command=lambda t=trans_type, i=trans_id: self.delete_transaction(t, i))
            delete_button.pack(side="left", padx=5)

    def delete_transaction(self, trans_type, trans_id):
        """Silme işlemi yapar ve listeyi günceller."""
        if trans_type == "income":
            delete_income(trans_id)
        else:
            delete_expense(trans_id)
        self.update_transaction_list()