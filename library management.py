books = []

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
        book = input("Enter book names: ")
        books.append(book)
        print("Books added successfully.")

    elif ch == 2:
        if len(books) == 0:
            print("No books in the library.")
        else:
            print("\nAvailable Books:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])

    elif ch == 3:
        book = input("Enter book name to search: ")
        if book in books:
            print("Book found.")
        else:
            print("Book not found.")

    elif ch == 4:
        book = input("Enter book name to issue: ")
        if book in books:
            books.remove(book)
            print("Book issued successfully.")
        else:
            print("Book is not available.")

    elif ch == 5:
        book = input("Enter book name to return: ")
        books.append(book)
        print("Book returned successfully.")

    elif ch == 6:
        book = input("Enter book name to delete: ")
        if book in books:
            books.remove(book)
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    elif ch == 7:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
