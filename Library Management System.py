
# Import mysql.connector module to connect python with sql to access the mysql server
import mysql.connector          

# mysql.connector module establishing the connection
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Dhanush2003@',
    database = 'librarydb'
) 

# mycursor is a variable. cursor() it is a fixed funtion to connect to the database 
mycursor = mydb.cursor() 
mycursor.execute("USE librarydb")

# function to insert book records

# Define a Function using insertbook name.
# whenevr call insertbook() it run the block of code.
# In variable q all the book data will be stored on placehoder '%s'. 
# Execute 'q' query with value 'data'. Send SQL command to MYSQL through the cursor.
# mydb.commit() is used for insert the record permanent.

def insertbook():
    bookno = int(input("Enter Book Number : "))
    bookname = input("Enter Book Name : ")
    bookauthor = input("Enter Book Author : ")
    bookprice = int(input("Enter Book Price : "))
    bookquantity = int(input("Enter Book Quantity : "))

    q = "INSERT INTO books VALUES(%s, %s, %s, %s, %s)"
    data = (bookno, bookname, bookauthor, bookprice, bookquantity)
    mycursor.execute(q,data)
    mydb.commit()
    print("Record Added Successfully")

# function to display book records

# q the query say select all the book from the table.
# .fetchall() gets all the rows returned by the query and stores them in data.
# count is used to show how any books in the table. rowcount is a property
# loop through each row in a data

def displaybook():
    q = "SELECT * FROM books"
    mycursor.execute(q)
    data = mycursor.fetchall()
    count = mycursor.rowcount 
    print("Total Book Records.....:", count)

    for (bookno,bookname,bookauthor,bookprice,bookquantity) in data:
        print("Book Number:", bookno)
        print("Book Name:",bookname)
        print("Book Author:",bookauthor)
        print("Book Price:",bookprice)
        print("Book Quantity:",bookquantity)
        print("----------------------------------")

# function to search book records

# Defines a function called searchbook.
# mycursor.execute(q, (bookno,)) execute expects the tuple/list dont want single integer the comma make itself as tuple.
# if count != 0 which means not equal to '0'.

def searchbook():
    bookno = int(input("Enter Book Number to Search : "))
    q = "SELECT * FROM books WHERE bookno=%s"
    mycursor.execute(q, (bookno,))
    data = mycursor.fetchall()
    count = mycursor.rowcount
    if count != 0:
        print("Book Records Found")
        for (bookno, bookname, bookauthor, bookprice, bookquantity) in data:
            print("Book Number:",bookno)
            print("Book Name:",bookname)
            print("Book Author:",bookauthor)
            print("Book Price:",bookprice)
            print("Book Quantity:",bookquantity)
            print("--------------------------------")

    else:
        print("Record Not Found..")

# funtion to delete a book record 

def deletebook():
    bookno = int(input("Enter the Book Number to be Deleted : "))
    q = "SELECT * FROM books WHERE bookno=%s"
    mycursor.execute(q, (bookno,))
    data = mycursor.fetchall()
    count = mycursor.rowcount

    if count != 0:
        print("Book Records found")
        for (bookno, bookname, bookauthor, bookprice, bookquantity) in data:
            print("Book Number:",bookno)
            print("Book Name:",bookname)
            print("Book Author:",bookauthor)
            print("Book Price:",bookprice)
            print("Book Quantity:",bookquantity)
            print("---------------------------")

        option = input("Are You Sure to DELETE above Record (Y/N)...: ")
        if option == "Y" or option == "y":
            q = "DELETE FROM books WHERE bookno=%s"
            mycursor.execute(q, (bookno,))
            print("Record Deleted Succcessfully")
            mydb.commit()
    else:
        print("Record Not Found")

# function to update book record
            
def updatebook():
    bookno = int(input("Enter the Book Number to be UPDATED : "))
    q = "SELECT * FROM books WHERE bookno=%s"
    mycursor.execute(q, (bookno,))
    data = mycursor.fetchall()
    count = mycursor.rowcount

    if count != 0:
        print("Book Records found")
        for (bookno, bookname, bookauthor, bookprice, bookquantity) in data:
            print("Book Number:",bookno)
            print("Book Name:",bookname)
            print("Book Author:",bookauthor)
            print("Book Price:",bookprice)
            print("Book Quantity:",bookquantity)
            print("---------------------------")

        option = input("Are You Sure to UPDATE above Record (Y/N)...: ")
        if option == "Y" or option == "y":
            print("Enter new data")
            bookname = input("Enter New Book Name:")
            bookauthor = input("Enter New Book Author")
            bookprice = int(input("Enter New Book Price:"))
            bookquantity = int(input("Enter New Book Quantity"))

            q = "UPDATE books SET bppkname=%s,bookauthor=%s,bookprice=%s,bookquantity=%s WHERE" 
            mycursor.execute(q, (bookno,))
            print("Record UPDATED Succcessfully")
            mydb.commit()
    else:
        print("Record Not Found")
 
# Code to display Menu 

while True :
    print("LIBRARY MANAGEMENT SYSTEM")
    print("===========================")
    print("1. Add New Book Record")
    print("2. Display Book Record")
    print("3. Search Book Record")
    print("4. Delete Book Record")
    print("5. Update Book Record")
    print("6. Exit")
    print("============================")
    choice = int(input("Enter Choice 1-6 : "))
    if choice == 1:
        insertbook()
    elif choice == 2:
        displaybook()
    elif choice == 3:
        searchbook()
    elif choice == 4:
        deletebook()
    elif choice == 5:
        updatebook()
    elif choice == 6:
        mydb.close()
        print("Thanks have a nice day.....")
        break
    else:
        print("Wrong Choice Please enter choice 1-6 : ")

