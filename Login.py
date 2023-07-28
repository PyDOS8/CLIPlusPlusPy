import os 
from cryptography.fernet import Fernet
def user():
    tries = 0
    if os.path.exists("username.txt"):
        os.system("CLI++Py.exe")
    else:
        username = input("Create a username > ")
        password = input("Create a password > ")
        password_bytes = password.encode("UTF-8")
        key = Fernet.generate_key() # create the key
        encrypted_password = Fernet.encrypt(password_bytes)
        with open("key.key", "w") as wf:
            wf.write(key) #Write the key to the file
            wf.close() # Close the file 
        with open("password.txt", "w") as wf:
            wf.write(encrypted_password)
            wf.close()
        with open("username.txt", "w") as wf:
            wf.write(username)
            wf.close()
user()
