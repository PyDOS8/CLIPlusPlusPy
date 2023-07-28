from cyptography.fernet import Fernet
import os
filedir = input("Enter a file or directory > ")
if os.path.exists(filedir):
  if os.path.isdir(filedir):
    with open("key.key", "rb") as key_file:
      encrypted_password = key_file.read()
      password = input("Enter you password > ").encode()
      decrypted_password = fernet.decrypt(encypted_password)
      if password == decrypted_password:
        os.removedirs(filedir)
      else:
        print("Access Denied!")
  else:
    with open("key.key" ) as key_file:
      encrypted_password = key_file.read()
      password = input("Enter your password > ").encode()
      decrypted_password = fernet.decrypt(encrypted_password)
      if password == decrypted_password:
        os.remove(filedir)
      else:
        print("Access Denied")
