from sqlalchemy.orm import sessionmaker
from models import engine, Income, Expense

#* Veritabanı session'u oluştur
SessionLocal = sessionmaker(bind=engine)

def add_income(amount, category, description):
    session = SessionLocal()
    new_income = Income(amount=amount, category=category, description=description)
    session.add(new_income)
    session.close()
    print("Gelir Başarıyla eklendi")

def get_all_income():
    session = SessionLocal()
    incomes = session.query(Income).all()
    session.close()
    return incomes

def update_income(income_id, new_amount=None, new_category=None, new_description=None):
    session = SessionLocal()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        if new_amount:
            income.amount = new_amount
        if new_category:
            income.category = new_category
        if new_description:
            income.description = new_description
        session.commit()
        print("Gelir başarıyla güncellendi")
    else:
        print("Gelir Bulunamadı.")
    session.close()

def delete_income(income_id):
    session = SessionLocal()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        session.delete(income)
        session.commit()
        print("Gelir başarıyla silindi")
    else:
        print("Gelir bulunamadı.")
    session.close()

def add_expense(amount, category, description):
    session = SessionLocal()
    new_expense = Expense(amount=amount, category=category, description=description)
    session.add(new_expense)
    session.commit()
    session.close()
    print("Gider Başarıyla eklendi.")

def get_all_expenses():
    session = SessionLocal()
    expenses = session.query(Expense).all()
    session.close()
    return expenses

def update_expense(expense_id, new_amount=None, new_category=None, new_description=None):
    session = SessionLocal()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        if new_amount:
            expense.amount = new_amount
        if new_category:
            expense.category = new_category
        if new_description:
            expense.description = new_description
        session.commit()
        print("Gider başarıyla güncellendi.")
    else:
        print("Gider bulunamadı.")
    session.close()

def delete_expense(expense_id):
    session = SessionLocal()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Gider başarıyla silindi.")
    else:
        print("Gider bulunamadı.")
    session.close()
