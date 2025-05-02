# Insider Knowledge

quick explanation:
- right from the start we notice that the data includes the phrase "Here is the decrypted flag: "
- xor one-time padding is vulnerable if we know some part of the plaintext (which is referred to as a crib)
- we also notice that the length of the key (24) is smaller than the length of the crib — which means that by XORing the first 24 letters of the ciphertext with our crib, we can obtain the key

using the key to XOR the entire ciphertext, we obtain `CTFSG{KN0W1NG_S0M3_PL41NT3XT_53RI0U5LY_H3LP3D}`