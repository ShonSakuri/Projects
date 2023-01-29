from Crypto.Cipher import DES
from Crypto.Util import number

import os
file = input(f"Please write the file name and extention:\n")
data = open(f"{file}","r")
def pad(text):
    text = text.encode()
    n = len(text) % 8
    return text + (b' ' * n)
d = data.read()
key = b'h1h2h3h4'
IV = os.urandom(8)
cipher = DES.new(key, DES.MODE_OFB,IV)
plaintext = pad(d)
msg = cipher.encrypt(plaintext)
print(msg)