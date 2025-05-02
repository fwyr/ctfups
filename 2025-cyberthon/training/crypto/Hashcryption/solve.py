# coding: utf-8
from pwn import *
from Crypto.Hash import MD5
from binascii import unhexlify

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}_"

alphadict = {}

for letter in letters:
    p = remote('chals.t.cyberthon25.ctf.sg', 32011)
    p.recvuntil("Data: ")
    p.send(letter)
    p.shutdown()
    p.recvline()
    p.recvline()
    p.recvline()
    leak = p.recvline().rstrip(b'\n')
    hexleak = leak.hex()
    alphadict[hexleak] = letter

enc = open('flag.txt.encrypted', 'rb').read().hex()
enc = ' '.join(enc[i:i + 32] for i in range(0, len(enc), 32))

print("Hello")
for i in list(enc.split(" ")):
    if i in alphadict:
        print(alphadict[i], end='')