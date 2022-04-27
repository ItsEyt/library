from sqlalchemy import Boolean, Column, Integer, String
from modules.db import Base

class Book(Base):
    __tablename__ = 'books'

    rowid = Column(Integer(), primary_key = True)
    name = Column(String(50), index = True)
    author = Column(String(50))
    year = Column(Integer())
    book_type = Column(Integer(), nullable = False)
    isloaned = Column(Boolean(), nullable = False, default = False)
