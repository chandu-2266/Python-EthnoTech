def project_student():
    students = []
    while True:
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            roll_no = input("Enter roll number: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            course = input("Enter course: ")
            student = {
                "roll_no": roll_no,
                "name": name,
                "age": age,
                "course": course
            }
            students.append(student)
            print("Student added successfully.")
        elif choice == "2":
            roll_no = input("Enter roll number to search: ")
            found = False
            for student in students:
                if student["roll_no"] == roll_no:
                    print("\nStudent Found")
                    print("Roll Number:", student["roll_no"])
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Course:", student["course"])
                    found = True
                    break
            if found == False:
                print("Student not found.")
        elif choice == "3":
            roll_no = input("Enter roll number to update: ")
            found = False
            for student in students:
                if student["roll_no"] == roll_no:
                    print("Enter new details")
                    student["name"] = input("Enter new name: ")
                    student["age"] = input("Enter new age: ")
                    student["course"] = input("Enter new course: ")
                    print("Student updated successfully.")
                    found = True
                    break
            if found == False:
                print("Student not found.")
        elif choice == "4":
            roll_no = input("Enter roll number to delete: ")
            found = False
            for student in students:
                if student["roll_no"] == roll_no:
                    students.remove(student)
                    print("Student deleted successfully.")
                    found = True
                    break
            if found == False:
                print("Student not found.")
        elif choice == "5":
            if len(students) == 0:
                print("No students available.")
            else:
                print("\nAll Students")
                for student in students:
                    print("--------------------")
                    print("Roll Number:", student["roll_no"])
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Course:", student["course"])
        elif choice == "6":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
project_student()