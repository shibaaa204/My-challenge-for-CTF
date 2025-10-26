from randcrack import RandCrack
from pwn import *

rc = RandCrack()
p=process(["python3", "chall.py"])
i = 0
while i < 624:
    p.sendline(b'1')
    num = p.recvline().split()[-1]
    rc.submit(int(num))
    i += 1
guess = rc.predict_getrandbits(32)
print(f"[+] Dự đoán số tiếp theo: {guess}")
p.sendline(str(guess).encode())
p.interactive()
