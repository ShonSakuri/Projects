## library ##
import string
import random
import requests
charlst = string.ascii_letters

length = len(charlst)
# print(type(charlst))

def run():
    s = True
    while s:
        result = ''.join(random.choices(charlst,k=8))
        res = f"{result}\n"
        with open("PasswordGenerator/passwords.txt","r") as r_file:
            r = r_file.read()
            if f'{result}' in r:
                s = False
        with open("PasswordGenerator/passwords.txt","a") as file:
            file.write(res)
run()