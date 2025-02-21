from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
#red= #b94949
#blue= #159541

#* Veritabanı bağlantısı kurulumu
DATABASE_URL = "sqlite:///budget_manager.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

#* Gelir Tablosu
class Income(Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True, autoincrement= True)
    amount = Column(Float,nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)

#* Gider Tablosu
class Expense(Base):
    __tablename__ = "expense"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)

#! Tabloları oluştur

if __name__ == "__main__":
    Base.metadata.create_all(engine)

