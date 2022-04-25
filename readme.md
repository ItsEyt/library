# Library web
## a web app for "loaning books online"

to run first install:

- SqlAlchemy
- Flask

On the log-in screen choose between 'user' and 'admin' for different features such as adding/removing books and customers or loaning and returning a book

admin features:
- see all books
- add a book
- remove a book
- search a book
- see all customers
- add a customer
- remove a customer
- search a customer
- see loans
- see late loans

user featuers:
- see all books
- loan a book
- return a book
- search a book
- see all customers
- search a customer
- see loans
- see late loans
---------------------

Features:
<!-- x - done / p - in progress -->
- [x] Add a customer          # addrow(newcustomer) // admin only
- [x] Add a book              # addrow(newbook)     // admin only
- [x] Loan a book             # addrow(newloan) + loanedbook(bookid) // from user selection. disables the option to loan the same book twice (unless the book has been returned)
- [x] Return a book           # returnloan(loanid, date) + isreturnlate(loanid) // from user selection. also checks if the return was late. adds book back to available loans
- [x] Display all books       # getdata(Book)       // loads the whole Book table         
- [x] Display all customers   # getdata(Customer)   // loads the whole Customer table
- [x] Display all loans        # getdata(Loans)     // loads the whole Loans
 table 
- [x] Display late loans
- [x] Find book by name       # books = getdata(Book, request.form.get('name'))         // loads books with 'name' in title instead of all books               
- [x] Find customer by name   # customers = getdata(Customer, request.form.get('name')) // loads customers with 'name' in name instead of all customers
- [x] Remove a book           # removerow(Book, request.args.get('rowid'))              // admin only
- [x] Remove a customer        # removerow(Customer, request.args.get('rowid'))          // admin only