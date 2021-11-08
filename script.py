import subprocess
import sys
import io
import string
import random
import os
p =[]
arr = []
f = io.open("4b.txt", mode="r", encoding="utf-8")
text = f.read()
arr = text.split()
c = list(string.ascii_letters + string.digits + "!@#$%ˆ&*()")
r = 0
print("Type d to delete or a to add a list of user:")
i = input()
if i == "a":
while r < len(arr):
username = arr[r]+arr[r+1]
try:
os.system("sudo useradd " + username)
print(f"User: "+username+" added")
os.system("sudo usermod -g" + "htlinn.4b " + username)
print(f"User: "+username+" added to group")
except:
print(f"Failed to add user.")
sys.exit(1)
r+=2
elif i == "d":
while r < len(arr):
username = arr[r]+arr[r+1]
try:
os.system("sudo userdel "+ username)
print(f"User: "+username+" deleted")
except:
print(f"Failed to delete user.")
sys.exit(1)
r+=2
else:
print("Not a possible input ")
