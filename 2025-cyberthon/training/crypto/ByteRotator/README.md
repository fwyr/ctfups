# ByteRotator

quick explanation:
- we notice that the encrypted file is "flag.jpg.encrypted"
- which means that the decrypted file must have the jpg magic bytes — FFD8FF

since the encryption code is essentially just a randomised caesar cipher (shift substitution cipher), we brute force all 256 different rotations and check whether the bytes "FFD8FF" show up.

when they do, we halt the program and get it to output the decrypted picture.

this gives us `CTFSG{b1gg3r_sh1ft5_m0r3_s3cur3}`