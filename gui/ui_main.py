import customtkinter as ctk
from ui_dashboard import DashboardFrame
from ui_income import IncomeFrame
from ui_expense import ExpenseFrame
from ui_reports import ReportsFrame
from ui_settings import SettingsFrame

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #* Ana pencere ayarları
        self.title("Budget Manager")
        self.geometry("900x600")
        self.resizable(False, False)
        ctk.set_appearance_mode("light")

        #* Ana yapı: 2 sütun (Yan Menü + İçerik)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #* Sidebar (Yan Menü) Sabit
        self.sidebar_width = 200
        self.sidebar = ctk.CTkFrame(self, width=self.sidebar_width, corner_radius=0, fg_color="#2c3e50")
        self.sidebar.grid(row=0, column=0, sticky="nsw")

        #* Menü Başlığı
        self.menu_label = ctk.CTkLabel(self.sidebar, text="Menü", font=("Arial", 16, "bold"))
        self.menu_label.pack(pady=10)

        #* Sayfa Butonları (Üste hizalanıyor)
        self.dashboard_btn = ctk.CTkButton(self.sidebar, text="Dashboard", command=self.show_dashboard)
        self.dashboard_btn.pack(pady=10, padx=8)

        self.income_btn = ctk.CTkButton(self.sidebar, text="Gelir Ekle", command=self.show_income)
        self.income_btn.pack(pady=10, padx=8)

        self.expense_btn = ctk.CTkButton(self.sidebar, text="Gider Ekle", command=self.show_expense)
        self.expense_btn.pack(pady=10, padx=8)

        self.reports_btn = ctk.CTkButton(self.sidebar, text="Raporlar", command=self.show_reports)
        self.reports_btn.pack(pady=10, padx=8)

        self.settings_btn = ctk.CTkButton(self.sidebar, text="⚙️", command=self.show_settings, width=30)
        self.settings_btn.pack(side="bottom", pady=20, padx=8)

        #* İçerik alanı (Geri kalan alanı kaplar)
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=4, pady=4)

        #* Varsayılan olarak dashboard'u göster
        self.current_frame = None
        self.show_dashboard()

    def show_frame(self, frame_class):
        """İçerik alanındaki çerçeveyi değiştir."""
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.content_frame)
        self.current_frame.pack(expand=True, fill="both")

    def show_dashboard(self):
        self.show_frame(DashboardFrame)

    def show_income(self):
        self.show_frame(IncomeFrame)
    
    def show_expense(self):
        self.show_frame(ExpenseFrame)
    
    def show_reports(self):
        self.show_frame(ReportsFrame)

    def show_settings(self):
        self.show_frame(SettingsFrame)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()