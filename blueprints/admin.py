import os
from flask import Blueprint, flash, redirect, render_template, request
from modules.books import Book
from modules.customers import Customer
from modules.loans import Loans
from modules.mainfunctions import getdata, addrow, removerow
from modules import filehelper as fh
from werkzeug.utils import secure_filename

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/home')
def admin_home():
    return render_template('index.html')

@admin.route('/books/', defaults={'action':''})
@admin.route('/books/<string:action>', methods=['GET','POST'])
def admin_books(action):
    if request.method == 'POST':
        if action == 'add':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and fh.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(fh.UPLOAD_FOLDER, filename))
            newbook = Book(name = request.form.get('name'), author = request.form.get('author'), \
                      year = request.form.get('year'), book_type = request.form.get('type'), picname = filename)
            addrow(newbook)
        if action == 'search': return render_template('books.html', action = action, books = getdata(Book, request.form.get('name')))
    elif request.method == 'GET': removerow(Book, request.args.get('rowid'))
    return render_template('books.html',action = action, books = getdata(Book))

@admin.route('/customers/', defaults={'action':''})
@admin.route('/customers/<string:action>', methods = ['GET','POST'])
def admin_customers(action):
    if request.method == 'POST':
        if action == 'add':
            newcustomer = Customer(name = request.form.get('name'),city = request.form.get('city'), age = request.form.get('age'))
            addrow(newcustomer)
        if action == 'search': return render_template('customers.html',action = action, customers = getdata(Customer, request.form.get('name')))
    elif request.method == 'GET': removerow(Customer, request.args.get('rowid'))
    return render_template('customers.html', action = action, customers = getdata(Customer))

@admin.route('/loans/', defaults={'action':''})
@admin.route('/loans/<string:action>', methods = ['POST','GET'])
def admin_loans(action):
    if action == 'late':
        return render_template('loans.html', loans = getdata(Loans, 'late')) 
    return render_template('loans.html', loans = getdata(Loans)) 

@admin.route('/about')
def admin_about():
    return render_template('about.html')