# Hashcryption

the script takes an input, hashes each character with MD5, then encrypts the hash with an unknown AES key.

note that the hash size for MD5 is 128 bits and that the AES is a 128-bit block cipher. this means that every character corresponds to 1 unique block, effectively making the script a substitution cipher.

we send all the necessary letters to the server and save it as a dictionary. then, we compare the encrypted flag to the dictionary to obtain its respective flag, hence getting the flag.

this gives us `CTFSGr0ng_m0d3_m1gh_45_3ll_d0n_3ncryp}` (which leads us to the correct flag `CTFSG{wr0ng_m0d3_m1gh_45_3ll_d0n_3ncrypt}`)