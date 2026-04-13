#Student management System using python

empdb = []  # Student Database

while True:
    choice = int(input("""\n\n\t\tMain Menu
       1: Insert student details
       2: Update student details
       3: Delete student details
       4: Show all students
       5: Search students
       6: Exit
       Enter your choice: """))

    if choice == 1:  # Insert student
        student = {}
        student["rollno"] = input("Enter Roll No: ")
        student["name"] = input("Enter Name: ")
        student["email"] = input("Enter Email: ")
        student["semester"] = input("Enter Semester: ")
        student["cgpa"] = input("Enter CGPA: ")
        empdb.append(student)
        print("\nStudent added successfully!")

    elif choice == 2:  # Update student details
        roll_no = input("Enter Roll No to update: ")
        found = False
        for student in empdb:
            if student["rollno"] == roll_no:
                print("Current details:", student)
                student["name"] = input("Enter New Name: ") or student["name"]
                student["email"] = input("Enter New Email: ") or student["email"]
                student["semester"] = input("Enter New Semester: ") or student["semester"]
                student["cgpa"] = input("Enter New CGPA: ") or student["cgpa"]
                print("\nStudent details updated!")
                found = True
                break
        if not found:
            print("\nStudent not found!")

    elif choice == 3:  # Delete student
        roll_no = input("Enter Roll No to delete: ")
        for student in empdb:
            if student["rollno"] == roll_no:
                empdb.remove(student)
                print("\nStudent deleted successfully!")
                break
        else:
            print("\nStudent not found!")

    elif choice == 4:  # Show all students
        if not empdb:
            print("\nNo students in the database!")
        else:
            print("\nStudent Records:")
            for student in empdb:
                print(student)

    elif choice == 5:  # Search student
        search_key = input("Enter Roll No or Name to search: ")
        found = False
        for student in empdb:
            if student["rollno"] == search_key or student["name"].lower() == search_key.lower():
                print("\nStudent Found:", student)
                found = True
                break
        if not found:
            print("\nStudent not found!")

    elif choice == 6:  # Exit
        print("\nExit!")
        break

    else:
        print("\nInvalid Choice!")