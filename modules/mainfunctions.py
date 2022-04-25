from datetime import timedelta
from database import mydatabase
from modules.books import Book
from modules.loans import Loans

#database connection
mydb = mydatabase.MyDB()

# brings all data from a table or specific data from the query(name of a book/customer)
def getdata(table, query = ''): # to get late returns query is used as a simple check but stays unused
    if query == '':
        if table == Loans:
            info = mydb.session.query(table).order_by(table.loan_date).all()
        else:    
            info = mydb.session.query(table).order_by(table.name).all()
    elif table == Loans:
        info = mydb.session.query(table).filter(table.islate == True).all()
    else:
        info = mydb.session.query(table).filter(table.name.like(f'%{query}%')).all()
    return info

# adds an object to his table
def addrow(row):
    with mydb.session as session:
        session.add(row)
        session.commit()

# removes an object from his table
def removerow(table,rid):
    with mydb.session as session:
        session.query(table).filter(table.rowid == rid).delete()
        session.commit()

def returnloan(loanid, date):
    with mydb.session as session:
        session.query(Loans).filter(Loans.loan_id == loanid).update({"return_date": date})
        for loan in session.query(Loans).filter(Loans.loan_id == loanid).all():
            loan.bookname.isloaned = False
        session.commit()

def isreturnlate(loanid):
    with mydb.session as session:
        for l in session.query(Loans).filter(Loans.loan_id == loanid).all():
            if l.bookname.book_type == 1:
                if l.return_date - l.loan_date < timedelta(days = 10):
                    session.query(Loans).filter(Loans.loan_id == loanid).update({"islate": False})
            elif l.bookname.book_type == 2:
                if l.return_date - l.loan_date < timedelta(days = 5):
                    session.query(Loans).filter(Loans.loan_id == loanid).update({"islate": False})
            else:
                if l.return_date - l.loan_date < timedelta(days = 2):
                    session.query(Loans).filter(Loans.loan_id == loanid).update({"islate": False})
        session.commit()

def loanedbook(bookid):
    with mydb.session as session:
        session.query(Book).filter(Book.rowid == bookid).update({"isloaned": True})
        session.commit()

def bookcheck(bookid):
    with mydb.session as session:
        for book in session.query(Book).filter(Book.rowid == bookid):
            if book.isloaned:
                return False
            return True
# adding a book
    # book1 = Book()                    # generate a new object for Book table
    # book1.book_name = 'harry potter'  # add parameters
    # book1.author = 'J.K rowling'      # add parameters
    # book1.book_type = 3               # add parameters
    # with mydb.session as session:     # open DB
    #     session.add(book1)            # add recent book object to table
    #     session.commit()              # commit 