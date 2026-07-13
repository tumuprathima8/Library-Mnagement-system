import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))

        cur.execute("INSERT INTO students(name,age,course,marks) VALUES(?,?,?,?)",
                    (name, age, course, marks))
        con.commit()

        print("Student Added Successfully")

    elif choice == "2":

        cur.execute("SELECT * FROM students")
        data = cur.fetchall()

        print("\nID\tName\tAge\tCourse\tMarks")
        print("-"*40)

        for i in data:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4])

    elif choice == "3":

        sid = int(input("Enter Student ID: "))

        cur.execute("SELECT * FROM students WHERE id=?", (sid,))
        student = cur.fetchone()

        if student:
            print(student)
        else:
            print("Student Not Found")

    elif choice == "4":

        sid = int(input("Enter Student ID: "))

        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = int(input("Enter New Marks: "))

        cur.execute(
            "UPDATE students SET name=?,age=?,course=?,marks=? WHERE id=?",
            (name, age, course, marks, sid)
        )

        con.commit()

        if cur.rowcount > 0:
            print("Student Updated Successfully")
        else:
            print("Student Not Found")

    elif choice == "5":

        sid = int(input("Enter Student ID: "))

        cur.execute("DELETE FROM students WHERE id=?", (sid,))
        con.commit()

        if cur.rowcount > 0:
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

con.close()