from pwnlib.util.fiddling import xor 

with open('flag.txt.encrypted', 'rb') as f:
    data = f.read()

crib = b"Here is the decrypted flag: "
key = xor(data[:24], crib[:24])
repeated_key = (key * 100)[:len(data)]
plaintext = xor(data, repeated_key)
print(plaintext.decode(errors="replace"))