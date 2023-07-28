import os 
from cryptography.fernet import Fernet
def user():
    tries = 0
    if os.path.exists("password.txt"):
        with open("key.key", "rb") as rf:
          key = rf.read()  
        f = Fernet(key)
        with open("password.txt", "rb") as password_file:
            encrypted_data = password_file.read()
            user_password = f.decrypt(encrypted_data).decode()
            password = input("Enter your password > ")
            if password == user_password:
                filedir = input("Enter a file or directory > ")
                if os.path.exists(filedir):
                    if os.path.isdir(filedir):
                        os.removedirs(filedir)
                    else:
                        os.remove(filedir)
                else:
                    print("The file or directory doesn't exist!")
            else:
                print("Access Denied!")
    else:
        username = input("Create a username > ")
        key = Fernet.generate_key() # Generates a key
        f = Fernet(key)
        password = input("Enter text > ").encode()
        encrypted_password = f.encrypt(password) # Encrypt the password
        decrypted_password = f.decrypt(encrypted_password)
        print(decrypted_password)
        with open("password.txt", "wb") as wf:
            wf.write(encrypted_password) # write the encrypted text to the password
        with open("key.key", "wb") as wf:
            wf.write(key)
user()
