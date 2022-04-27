from sqlalchemy import Column, Integer, String
from modules.db import Base

class Customer(Base):
    __tablename__ = 'customers'

    rowid = Column(Integer(), primary_key = True)
    name = Column(String(50), nullable = False)
    city = Column(String())
    age = Column(Integer())