import hashlib
import os

def hash(s):
    return hashlib.md5(s.encode()).hexdigest()
command=[]
hashlist=[]
while True:
    cmd=input(">>> ")
    if hash(cmd) not in hashlist:
        command.append(cmd)
        hashlist.append(hash(cmd))
        continue
    if cmd not in command and "Hash Collision" in cmd:
        print("win")
