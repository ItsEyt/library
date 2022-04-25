import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Column, Integer, String, ForeignKey, null
from modules import books, customers, db
from sqlalchemy.orm import relationship


class Loans(db.Base):
    __tablename__ = 'loans'

    loan_id = Column(Integer(), primary_key = True)
    custID = Column(Integer(), ForeignKey(customers.Customer.rowid))
    bookID = Column(Integer(), ForeignKey(books.Book.rowid))
    loan_date = Column(DateTime())
    return_date = Column(DateTime())
    islate = Column(Boolean(), default = True, nullable = False)

    customername = relationship("Customer", foreign_keys = custID)
    bookname = relationship("Book", foreign_keys = bookID)