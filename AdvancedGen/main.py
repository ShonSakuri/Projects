## library ##
import string
import random
import pyperclip

all = string.digits + string.ascii_lowercase + string.ascii_uppercase
letters = string.ascii_lowercase + string.ascii_uppercase
digits = string.digits

print("""
1 - With All Characters
2 - Just with Letters
3 - Just Digits
""")
Format_inp = input("Enter format option: ")
# print(type(Format_inp))
lst = ["1", "2", "3"]
if Format_inp not in lst:
    "You have to write a number between 1 to 3.."
    exit()
print("""
Enter the password length (1-20)
""")
Length_inp = input("Enter length: ")
lst2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
if Length_inp not in lst2:
    "You have to write a number between 1 to 20.."
    exit()


def PassWord(Length, Format):
    if Format == "1":
        Format = all
    if Format == "2":
        Format = letters
    if Format == "3":
        Format = digits
    print(type(Length))
    result = ''.join(random.choices(Format, k=int(Length)))
    print(result)
    pyperclip.copy(result)
    print("Password copied to clipboard.")


PassWord(Length_inp, Format_inp)
