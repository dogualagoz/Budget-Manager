from sqlalchemy.orm import sessionmaker
from models import engine, Income, Expense

#* Veritabanı session'u oluştur
SessionLocal = sessionmaker(bind=engine)

def add_income(amount, category, description):
    pass

def get_all_income():
    pass

def update_income(income_id, new_amount=None, new_category=None, new_description=None):
    pass

def delete_income(income_id):
    pass

def add_expense(amount, category, description):
    pass

def get_all_expenses():
    pass

def update_expense(expense_id, new_amount=None, new_category=None, new_description=None):
    pass

def delete_expense(expense_id):
    pass
