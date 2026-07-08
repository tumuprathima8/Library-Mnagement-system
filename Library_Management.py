import sqlite3

con = sqlite3.connect("library.db")
cur = con.cursor()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        book = input("Enter book name: ")
        cur.execute("INSERT INTO books(name) VALUES(?)", (book,))
        con.commit()
        print("Book added successfully.")

    elif ch == 2:
        cur.execute("SELECT * FROM books")
        books = cur.fetchall()

        if len(books) == 0:
            print("No books in the library.")
        else:
            for i in range(len(books)):
                print(i+1, ".", books[i][1])

    elif ch == 3:
        book = input("Enter book name to search: ")
        cur.execute("SELECT * FROM books WHERE name=?", (book,))
        result = cur.fetchone()

        if result:
            print("Book found!")
        else:
            print("Book not found!")

    elif ch == 4:
        book = input("Enter book to issue: ")
        cur.execute("SELECT * FROM books WHERE name=?", (book,))
        result = cur.fetchone()

        if result:
            cur.execute("DELETE FROM books WHERE name=?", (book,))
            con.commit()
            print("Book issued successfully.")
        else:
            print("Book not available.")
    elif ch == 5:
        book = input("Enter book to return: ")
        cur.execute("INSERT INTO books(name) VALUES(?)", (book,))
        con.commit()
        print("Book returned successfully.")

    elif ch == 6:
        book = input("Enter book to delete: ")
        cur.execute("SELECT * FROM books WHERE name=?", (book,))
        result = cur.fetchone()

        if result:
            cur.execute("DELETE FROM books WHERE name=?", (book,))
            con.commit()
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    elif ch == 7:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")

con.close()