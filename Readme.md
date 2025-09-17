# Library Management System (Python & MySQL)

## Short Description
Python CLI Library Management System using MySQL. Allows adding, displaying, searching, updating, and deleting book records. Simple terminal-based app to manage library inventory efficiently for small-scale setups.

## Description
A simple Python command-line Library Management System that interacts with a MySQL database to manage books. The system allows users to add, display, search, update, and delete book records efficiently.

## Problem Statement
Managing a library manually can be error-prone and time-consuming. Tracking book inventory, updates, and records without automation leads to mistakes and inefficiency, especially in small libraries.

## Solution
This Python CLI app automates library management by connecting to a MySQL database. Users can quickly perform all CRUD (Create, Read, Update, Delete) operations on book records from a terminal interface.

## Technologies Used
- Python 3.x
- MySQL Database
- mysql-connector-python

## Features
- Add new book records
- Display all books
- Search for a book by its number
- Update book details
- Delete book records

## Installation & Usage
1. pip install mysql-connector-python

2. Setup Mysql DataBase and Table
CREATE DATABASE librarydb;
CREATE TABLE books (
    bookno INT PRIMARY KEY,
    bookname VARCHAR(255),
    bookauthor VARCHAR(255),
    bookprice INT,
    bookquantity INT
);
3. Run The Program
python library_management.py

