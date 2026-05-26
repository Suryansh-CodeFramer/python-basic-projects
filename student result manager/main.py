# student result manager

# conditional - logic
# loops- menu system
# dictionary- to store data
#
# Teacher:
# 1-add student
# 2- view all students
# 3- check result
# 4- exit

student ={}

while True:
    print("\n --student manager app-- ")
    print("1. Add student")
    print("2. view student")
    print("3. check student results")
    print("4. exit")
    choice = input("Enter your choice: ")
    #Add student
    if choice == "1":
        name=input("Enter student name: ")
        marks=int(input("Enter student marks: "))
        student[name]=marks
        print(f"{name}'s marks: {marks} successfully added !")

    #view students
    elif choice =="2":
        if not student:
            print("no student found!")
        else:
            for name, marks in student.items():
                print(name , " : ",marks)

    #check result
    elif choice =="3":
        name = input("Enter student name: ")
        if name in student:
            marks = student[name]
            if marks>=40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found!")
    #exit
    elif choice=="4":
        print("exit")
        break
    else:
        print("Please enter a valid choice")


