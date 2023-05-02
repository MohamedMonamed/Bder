import sqlite3

# توصيل قاعدة البيانات
conn = sqlite3.connect('library.db')

# إنشاء جدول الكتب
conn.execute('''
CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
author TEXT NOT NULL,
publisher TEXT NOT NULL,
available INTEGER DEFAULT 1)
''')

# إضافة كتاب جديد
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    publisher = input("Enter book publisher: ")
    conn.execute(f"INSERT INTO books(title, author, publisher) VALUES ('{title}', '{author}', '{publisher}')")
    conn.commit()
    print("Book added successfully!")

# عرض جميع الكتب المتاحة
def view_available_books():
    cursor = conn.execute("SELECT id, title, author, publisher FROM books WHERE available=1")
    print("{:<5} {:<25} {:<20} {:<20}".format('ID', 'Title', 'Author', 'Publisher'))
    for row in cursor:
        print("{:<5} {:<25} {:<20} {:<20}".format(row[0], row[1], row[2], row[3]))

# بحث عن كتاب بالعنوان
def search_book():
    title = input("Enter book title: ")
    cursor = conn.execute(f"SELECT id, title, author, publisher FROM books WHERE title LIKE '%{title}%' AND available=1")
    if cursor.fetchone() is None:
        print("No results found!")
    else:
        print("{:<5} {:<25} {:<20} {:<20}".format('ID', 'Title', 'Author', 'Publisher'))
        for row in cursor:
            print("{:<5} {:<25} {:<20} {:<20}".format(row[0], row[1], row[2], row[3]))

# إعارة كتاب
def borrow_book():
    book_id = input("Enter book ID: ")
    cursor = conn.execute(f"SELECT available FROM books WHERE id={book_id}")
    row = cursor.fetchone()
    if row is None:
        print("Invalid book ID!")
    elif row[0] == 0:
        print("This book is already borrowed!")
    else:
        conn.execute(f"UPDATE books SET available=0 WHERE id={book_id}")
        conn.commit()
        print("Book borrowed successfully!")

# إعادة كتاب
def return_book():
    book_id = input("Enter book ID: ")
    cursor = conn.execute(f"SELECT available FROM books WHERE id={book_id}")
    row = cursor.fetchone()
    if row is None:
        print("Invalid book ID!")
    elif row[0] == 1:
        print("This book is not borrowed!")
    else:
        conn.execute(f"UPDATE books SET available=1 WHERE id={book_id}")
        conn.commit()
        print("Book returned successfully!")

# القائمة الرئيس





