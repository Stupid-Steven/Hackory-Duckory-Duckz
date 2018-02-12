#!/usr/bin/env python3

import binascii
#Original File Name "91afa7cbc1339d19d0245292cca77ed6ce7a99dfd37b577fdffdc5b1c3a8dfb3_mystery"
#Sample Output: "6523c2b5772bc389206c0b3ac2bfc2acc287c3a737c380c2b30ac297c39c3729641159133903"

key = "mBcZRYaq"

def encrypt(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))

def decrypt(s):
    output = ""
    
    r = binascii.unhexlify(bytes(s, "utf-8"))
    
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return output