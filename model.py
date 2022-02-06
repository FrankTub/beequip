from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    coc_number = Column(String)
    name = Column(String)


class Installments(Base):
    __tablename__ = "installments"
    installment_no = Column(String, primary_key=True)
    t = Column(Integer)
    date = Column(String)
    installment = Column(Float)
    principal = Column(Float)
    interest = Column(Float)
    outstanding_start = Column(Float)

class Leases(Base):
    __tablename__ = "leases"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    reference = Column(String)
    installment_no = Column(String, ForeignKey("installments.installment_no"))
    lane = Column(String)
    team = Column(String)
    object_brand = Column(String)
    object_type = Column(String)