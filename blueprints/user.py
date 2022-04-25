from flask import Blueprint, render_template, request
from modules.books import Book
from modules.customers import Customer
from modules.loans import Loans
from modules.mainfunctions import addrow, bookcheck, getdata, isreturnlate, loanedbook, returnloan
from datetime import datetime

user = Blueprint('user',__name__,url_prefix='/user')

# home route
@user.route('/home')
def user_home():
    return render_template('index.html')

# book collection route
@user.route('/books/',defaults={'action':''})
@user.route('/books/<string:action>', methods = ['GET', 'POST'])
def user_books(action):
    if request.method == 'POST':
        if action == 'search': return render_template('books.html', action = action, books = getdata(Book, request.form.get('name')))
    return render_template('books.html',action=action, books = getdata(Book), customers = getdata(Customer))

# loan collection route
@user.route('/loans/',defaults={'action':''},methods = ['GET','POST'])
@user.route('/loans/<string:action>', methods = ['GET', 'POST'])
def user_loans(action):
    if request.method == 'GET':
        if bookcheck(request.args.get('bookid')):
            newloan = Loans(custID = request.args.get('customerid'), bookID = request.args.get('bookid'), loan_date = datetime.now().date())
            addrow(newloan)
            loanedbook(request.args.get('bookid'))
    elif request.method == 'POST':
        loanid = request.form.get('loanid')
        returndate = datetime.strptime(request.form['returndate'],'%Y-%m-%d')
        returnloan(loanid, returndate)
        isreturnlate(loanid)
    if action == 'late':
        return render_template('loans.html', loans = getdata(Loans, 'late'))
    return render_template('loans.html', loans = getdata(Loans))

# customer collection route
@user.route('/customers/', defaults={'action':''})
@user.route('/customers/<string:action>', methods = ['GET', 'POST'])
def user_customers(action):
    if action == 'search': return render_template('customers.html',action = action, customers = getdata(Customer, request.form.get('name')))
    return render_template('customers.html',action = action, customers = getdata(Customer))