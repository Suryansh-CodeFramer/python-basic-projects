# Student Result Manager with File Handling

student = {}

# --- LOAD DATA FROM FILE

try:
    with open("students.txt", "r") as file:

        # read each line from file
        for line in file:

            # remove extra newline (\n)
            line = line.strip()

            # split using comma
            name, marks = line.split(",")

            # store in dictionary
            student[name] = int(marks)

except FileNotFoundError:
    # if file does not exist
    print("No previous student record found!")

# --- MENU SYSTEM

while True:

    print("\n----- STUDENT MANAGER APP -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Student Result")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ---ADD STUDENT

    if choice == "1":

        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))

        # add in dictionary
        student[name] = marks

        # save in file
        with open("students.txt", "a") as file:
            file.write(f"{name},{marks}\n")

        print(f"{name}'s marks added successfully!")

    # ---VIEW STUDENTS

    elif choice == "2":

        if not student:
            print("No students found!")

        else:
            print("\nStudent Records:\n")

            for name, marks in student.items():
                print(name, ":", marks)

    # --- CHECK RESULT

    elif choice == "3":

        name = input("Enter student name: ")

        if name in student:

            marks = student[name]

            if marks >= 40:
                result = "Pass"

            else:
                result = "Fail"

            print(f"{name} : {result}")

            # save result history
            with open("results.txt", "a") as file:
                file.write(f"{name} : {result}\n")

        else:
            print("Student not found!")

    # --- UPDATE MARKS

    elif choice == "4":

        name = input("Enter student name: ")

        if name in student:

            new_marks = int(input("Enter new marks: "))

            # update dictionary
            student[name] = new_marks

            # rewrite whole file
            with open("students.txt", "w") as file:

                for name, marks in student.items():
                    file.write(f"{name},{marks}\n")

            print("Marks updated successfully!")

        else:
            print("Student not found!")

    # --- DELETE STUDENT

    elif choice == "5":

        name = input("Enter student name: ")

        if name in student:

            # delete from dictionary
            del student[name]

            # rewrite file after deletion
            with open("students.txt", "w") as file:

                for name, marks in student.items():
                    file.write(f"{name},{marks}\n")

            print("Student deleted successfully!")

        else:
            print("Student not found!")

    # --- EXIT

    elif choice == "6":

        print("Exiting program...")
        break

    # --- INVALID CHOICE

    else:
        print("Please enter a valid choice!")