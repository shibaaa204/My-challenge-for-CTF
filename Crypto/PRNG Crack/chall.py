import time, random
import os

random.seed(time.time())
while True:
    guest=random.getrandbits(32)
    cmd=int(input(">>> "))
    if cmd==guest:
        print("win")
    else:
        print(guest)
