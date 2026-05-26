import random
import string

password={}
# load exiting passwor file

try:
    with open("password.txt","r") as file:
        for line in file:
            website,pwd =line.strip().split(":")
            password[website] = pwd
except:
    pass

def generate_password():
    chars =string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for i in range(8))
    return password
while True:
    print("Welcome to Password Manager")
    print("1. save password")
    print("2. view password")
    print("3. generate password")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    #Save password

    if choice == 1:
        site=input("Enter website name:")
        pwd=input("Enter password:")
        password[site] = pwd
        with open("password.txt","a") as file:
            file.write(f"{site}:{pwd}\n")
        print("Password saved")

    #View password

    elif choice == 2:
        if not password:
            print("no data found")
        else:
            for site,pwd in password.items():
                print(site,":",pwd)


    #Generate Password
    elif choice == 3:
        print("generating password", generate_password())
    #Exit
    elif choice == "4":

        print("Exiting program...")
        break
    #invalid choice
    else:
        print("Please enter a valid choice!")


