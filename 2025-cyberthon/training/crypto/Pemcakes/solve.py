from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

with open("pubkey.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

if hasattr(public_key, "public_numbers"):
    numbers = public_key.public_numbers()
    modulus = numbers.n
    exponent = numbers.e

    print("Modulus (n):", modulus)
    print("Exponent (e):", exponent)
else:
    print("Not an RSA key.")

from Crypto.Util.number import bytes_to_long, long_to_bytes

with open('flag.txt.encrypted', 'rb') as f:
    data = f.read()

c = bytes_to_long(data)
print(f"Ciphertext (c)): {c}")
 
from math import isqrt
print("---")
m = isqrt(c)
print(long_to_bytes(m))