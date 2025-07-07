import hashlib
import getpass

password_manager = {}
def create():
    print("-------------------------------------------------")
    username = input("username: ")
    password = getpass.getpass("password: ")
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hash_password
    print("Account created successfully!")
    print("-------------------------------------------------")
def login():
    print("-------------------------------------------------")
    username = input("username: ")
    password = getpass.getpass("password: ")
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hash_password:
        print("Welcome back!", username)
    else:
        print("User not found, try again...")
    print("-------------------------------------------------")

def main():
    while True:
        choice = input("Enter \n1 to CREATE ACCOUNT, \n2 to LOGIN, \n3 to EXIT\n")
        if choice == "1":
            create()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid number...")

if __name__ == "__main__":
    main()
