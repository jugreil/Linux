
import sys
import io
import os

p =[]
arr = []
reader = io.open("4b.txt", mode="r", encoding="utf-8")
text = reader.read()
arr = text.split()
i = 0
print("Type --del to delete or --add to add a list of user:")
input = input()
if input == "a":
    while i < len(arr):
        username = arr[i]+arr[i+1]
        try:
            os.system("sudo useradd " + username)
            print(f"User: "+username+" added")
            os.system("sudo usermod -g" + "htlinn.4b " + username)
            print(f"User: "+username+" added to group")
        except:
            print(f"Failed to add user.")
            sys.exit(1)
        i+=2
elif input == "d":
    while i < len(arr):
        username = arr[i]+arr[i+1]
        try:
            os.system("sudo userdel "+ username)
            print(f"User: "+username+" deleted")
        except:
            print(f"Failed to delete user.")
            sys.exit(1)
        i+=2
else:
    print("Not a possible input ")
