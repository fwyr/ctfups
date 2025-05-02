# Pemcakes

okay
- `pubkey.pem` contains your modulus n and public key exponent e
- you can just use a python library to extract it from the .pem file itself

we notice that e is actually quite small and n is quite large comparably.
- the RSA cryptosystem dictates that the plaintext-to-ciphertext conversion is $c \equiv m^e  \pmod{n}$
- but since $e = 2$ is small, could $c$ really just be equal to $m^2$?
- we test it out by square-rooting $n$ to obtain our supposed plaintext $m$

converting $m$ to bytes, we see that it really is a small exponent attack! this gives us `CTFSG{P3MC4K35_4R3_3NCRYPT3D_P4NC4K35}`