import os 
from cryptography.fernet import Fernet
def user():
    if not os.path.exists("username.txt"):
        os.system("CLI++Py.exe")
    else:
        username = input("Create a username > ")
        key = Fernet.generate_key() # Generates a key
        f = Fernet(key)
        password = input("Enter text > ").encode()
        encrypted_text = f.encrypt(password) # Encrypt the password
        with open("password.txt", "wb") as wf:
            wf.write(encrypted_text) # write the encrypted text to the password
        with open("username.txt", "w") as wf:
            wf.write(username)
user()
