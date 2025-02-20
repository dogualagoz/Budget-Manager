import customtkinter as ctk

class TransactionFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#1e1e1e", corner_radius=10)

        # Başlık
        self.header_label = ctk.CTkLabel(self, text="Gelir & Gider Ekle", font=("Arial", 20, "bold"), text_color="white")
        self.header_label.pack(pady=15)

        # Açıklama Alanı
        self.description_label = ctk.CTkLabel(self, text="Açıklama:", font=("Arial", 14), text_color="white")
        self.description_label.pack(anchor="w", padx=20)
        self.description_entry = ctk.CTkEntry(self, placeholder_text="Açıklama girin...", width=300)
        self.description_entry.pack(pady=5, padx=20)

        # Kategori Alanı
        self.category_label = ctk.CTkLabel(self, text="Kategori:", font=("Arial", 14), text_color="white")
        self.category_label.pack(anchor="w", padx=20)
        self.category_entry = ctk.CTkEntry(self, placeholder_text="Kategori girin...", width=300)
        self.category_entry.pack(pady=5, padx=20)

        # Miktar Alanı
        self.amount_label = ctk.CTkLabel(self, text="Miktar:", font=("Arial", 14), text_color="white")
        self.amount_label.pack(anchor="w", padx=20)
        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Miktar girin...", width=300)
        self.amount_entry.pack(pady=5, padx=20)

        # Butonlar (Gelir Ekle - Yeşil, Gider Ekle - Kırmızı)
        self.button_frame = ctk.CTkFrame(self, fg_color="#1e1e1e")
        self.button_frame.pack(pady=15)

        self.add_income_button = ctk.CTkButton(self.button_frame, text="Gelir Ekle", fg_color="#27ae60", text_color="white", hover_color="#1e8449", width=140)
        self.add_income_button.pack(side="left", padx=10)

        self.add_expense_button = ctk.CTkButton(self.button_frame, text="Gider Ekle", fg_color="#e74c3c", text_color="white", hover_color="#c0392b", width=140)
        self.add_expense_button.pack(side="left", padx=10)