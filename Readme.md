# 📚 Library Management System (Python + MySQL)

A simple **command-line Library Management System** built with **Python** and **MySQL**. This project allows you to manage books by adding, viewing, searching, updating, and deleting records efficiently.

---

## 🚀 Features

* ➕ **Add Book** – Insert new book records with number, name, author, price, and quantity.
* 📜 **Display Books** – View all stored book records.
* 🔍 **Search Book by Number** – Quickly find a book by its unique number.
* ❌ **Delete Book** – Remove specific book entries.
* ✏️ **Update Book** – Modify existing book details.
* 🚪 **Exit System** – Close the program safely.

---

## ⚙️ Setup & Installation

### 1. Install Requirements

Make sure Python is installed, then install the MySQL connector:

```bash
pip install mysql-connector-python
```

### 2. Setup MySQL Database

1. Open MySQL and create a new database:

   ```sql
   CREATE DATABASE librarydb;
   ```

2. Create a `books` table inside `librarydb`:

   ```sql
   CREATE TABLE books (
       bookno INT PRIMARY KEY,
       bookname VARCHAR(150) NOT NULL,
       bookauthor VARCHAR(150) NOT NULL,
       bookprice DECIMAL(10,2) NOT NULL,
       bookquantity INT NOT NULL
   );
   ```

### 3. Connect Python to MySQL

Update the connection details in your script if needed:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",          # your MySQL username
    password="password",  # your MySQL password
    database="librarydb"   # database name
)
```

---

## ▶️ How It Works (Procedure)

1. **Run the script**:

   ```bash
   python library_management.py
   ```

2. **Menu Options**:

   * `1` → Add a new book
   * `2` → Display all books
   * `3` → Search book by number
   * `4` → Delete book record
   * `5` → Update book record
   * `6` → Exit program

3. **Example Flow**:

   * User selects `1` → Enters details → Book is saved in MySQL.
   * User selects `2` → Displays all book records.
   * User selects `5` → Updates details of an existing book.

---

## 📂 Project Structure

```
📦 library-management-system
 ┣ 📜 library_management.py   # Main script
 ┣ 📜 README.md               # Documentation
```

---

## 🛠️ Tech Stack

* **Python** (for backend logic)
* **MySQL** (for database)

---

## 📌 Future Improvements

* Add book issue/return system.
* Track borrowers and due dates.
* Generate reports of books available vs issued.
* Export book list to CSV/Excel.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to suggest new features or improvements.

---

## 📧 Contact

Created by **Dhanush** – If you like this project, give it a ⭐ on GitHub!
