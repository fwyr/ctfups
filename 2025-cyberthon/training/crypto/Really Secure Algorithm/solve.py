from Crypto.Util.number import bytes_to_long

with open('flag.txt.encrypted', 'rb') as f:
    data = f.read()

with open('flag.txt', 'w') as f:
    print(str(bytes_to_long(data)))

# this is to print out the ciphertext from the encrypted file