## library ##
import string
import random
import requests
charlst = string.ascii_letters

length = len(charlst)
# print(type(charlst))

def run():
    password = "sak"
    while True:
        result = ''.join(random.choices(charlst,k=3))
        if result == password:
            print("success!")
            break
run()