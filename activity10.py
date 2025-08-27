
from getpass import getpass

username = 'Jeuz'
pword = 'jeuz1234'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if (u == username) and (p == pword) :

         print("Access Granted")
else:
         print("Access Denied")