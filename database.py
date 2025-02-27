from sqlalchemy.orm import sessionmaker
from models import engine, Income, Expense
from sqlalchemy import func

#* Veritabanı session'u oluştur
SessionLocal = sessionmaker(bind=engine, autoflush=False)

def add_income(amount, category, description):
    session = SessionLocal()
    try:
        new_income = Income(amount=amount, category=category, description=description)
        session.add(new_income)
        session.commit()  # <-- Eksik olan commit eklendi
        print("Gelir Başarıyla eklendi")
    except Exception as e:
        session.rollback()  # Hata olursa değişiklikleri geri al
        print(f"Hata oluştu: {e}")
    finally:
        session.close()  # Her durumda session kapatılır

def get_all_income():
    session = SessionLocal()
    try:
        incomes = session.query(Income).all()
        session.close()
        return incomes if incomes else []
    finally:
        session.close()

def update_income(income_id, new_amount=None, new_category=None, new_description=None):
    session = SessionLocal()
    try:
        income = session.query(Income).filter_by(id=income_id).first()
        if income:
            if new_amount:
                income.amount = new_amount
            if new_category:
                income.category = new_category
            if new_description:
                income.description = new_description
            session.commit()  # <-- Eksik commit eklendi
            print("Gelir başarıyla güncellendi")
        else:
            print("Gelir Bulunamadı.")
    except Exception as e:
        session.rollback()
        print(f"Hata oluştu: {e}")
    finally:
        session.close()

def delete_income(income_id):
    session = SessionLocal()
    try:
        income = session.query(Income).filter_by(id=income_id).first()
        if income:
            session.delete(income)
            session.commit()  # <-- Eksik commit eklendi
            print("Gelir başarıyla silindi")
        else:
            print("Gelir bulunamadı.")
    except Exception as e:
        session.rollback()
        print(f"Hata oluştu: {e}")
    finally:
        session.close()

def add_expense(amount, category, description):
    session = SessionLocal()
    try:
        new_expense = Expense(amount=amount, category=category, description=description)
        session.add(new_expense)
        session.commit()  # <-- Eksik olan commit eklendi
        print("Gider Başarıyla eklendi.")
    except Exception as e:
        session.rollback()
        print(f"Hata oluştu: {e}")
    finally:
        session.close()

def get_all_expenses():
    session = SessionLocal()
    try:
        expenses = session.query(Expense).all()
        session.close()
        return expenses if expenses else []
    finally:
        session.close()


def update_expense(expense_id, new_amount=None, new_category=None, new_description=None):
    session = SessionLocal()
    try:
        expense = session.query(Expense).filter_by(id=expense_id).first()
        if expense:
            if new_amount:
                expense.amount = new_amount
            if new_category:
                expense.category = new_category
            if new_description:
                expense.description = new_description
            session.commit()  # <-- Eksik commit eklendi
            print("Gider başarıyla güncellendi.")
        else:
            print("Gider bulunamadı.")
    except Exception as e:
        session.rollback()
        print(f"Hata oluştu: {e}")
    finally:
        session.close()

def delete_expense(expense_id):
    session = SessionLocal()
    try:
        expense = session.query(Expense).filter_by(id=expense_id).first()
        if expense:
            session.delete(expense)
            session.commit()  # <-- Eksik commit eklendi
            print("Gider başarıyla silindi.")
        else:
            print("Gider bulunamadı.")
    except Exception as e:
        session.rollback()
        print(f"Hata oluştu: {e}")
    finally:
        session.close()

def get_total_income():
    """Veritabanından toplam gelir miktarını döndürür."""
    session = SessionLocal()
    total_income = session.query(func.sum(Income.amount)).scalar() or 0
    session.close()
    return total_income

def get_total_expense():
    """Veritabanından toplam gider miktarını döndürür."""
    session = SessionLocal()
    total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
    session.close()
    return total_expense

from sqlalchemy import desc

def get_recent_transactions(limit=15):
    """Son 15 işlemi tarihe göre sıralayarak getirir (Gelir ve Gider birlikte)."""
    session = SessionLocal()
    
    # Gelirleri çek
    incomes = session.query(Income.id, Income.amount, Income.category, Income.date).all()
    incomes = [("income", inc.category, inc.amount, inc.date) for inc in incomes]

    # Giderleri çek
    expenses = session.query(Expense.id, Expense.amount, Expense.category, Expense.date).all()
    expenses = [("expense", exp.category, exp.amount, exp.date) for exp in expenses]

    # Gelir ve giderleri birleştir, tarihe göre sıralayıp en güncel 15 işlemi al
    transactions = incomes + expenses
    transactions.sort(key=lambda x: x[3], reverse=True)  # Tarihe göre sıralama (En yeni en üstte)
    
    session.close()
    return transactions[:limit]  # Son 15 işlem