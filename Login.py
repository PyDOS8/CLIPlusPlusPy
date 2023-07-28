import os 
import binascii
def user():
    tries = 0
    if os.path.exists("username.txt"):
        username = open("username.txt", "r")
        Username = input("Enter your username ")
        if Username == username.read():
            password = open("password.txt", "r")
            password_bytes = binascii.unhexlify(password.read().strip())
            password_str = password_bytes.decode('utf-8')
            Password = input("Enter your password ")
            if Password == password_str:
                username = open("username.txt", "r")
                print("Welcome Back ", username.read())
                username.close()
                os.system("start CLI++Py.exe");
            else:
                if not tries == 3:
                    print("Incorrect Password!")
                    tries = tries+1
                    user()
                else:
                    print("Access Denied")
        else:
            if not tries == 3:
                print("Incorrect Username")
                tries = tries+1
                user()
            else:
                print("Access Denied!")
    else:
        username = input("Create a username > ")
        password = input("Create a password > ")
        password_bytes = password.encode("UTF-8")
        Username = open("username.txt", "w")
        Username.write(username)
        Username.close()
        Password = open("password.txt", "wb")
        password_hex = binascii.hexlify(password_bytes)
        Password.write(password_hex)
        Password.close()
user()
