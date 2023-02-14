import pymongo
import sys
import tty
import os
import termios
from colorama import Fore, Style
import getpass
import time
import hashlib


class Database:
    client = pymongo.MongoClient(
        "mongodb+srv://shon:SeanSak123@cluster0.wrckk3j.mongodb.net")
    db = client["Bank"]
    collection = db["users"]


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def contract():
    os.system("clear")
    print(Fore.BLUE, """
    Denied - Click [N]
    Agree - Click [Y]
    """)
    char = getch()

    if char == "n":
        return "n"
    elif char == "y":
        return "y"


def menu():
    print(Fore.LIGHTMAGENTA_EX, """
    1. Contract, Register
    2. Login
    3. Reset Password
    """)
    print(Style.RESET_ALL)


def admin():
    tr = True
    while tr:
        commands = ["user", "removemoney", "addmoney",
                    "quit", "setmoney", "deleteuser"]
        print(Fore.YELLOW, commands)
        print(Style.RESET_ALL)
        command = input("command <-> ").lower()

        if command == "quit":
            tr = False

        elif command == "removemoney":
            usr = input("user <-> ")
            user = Database.collection.find_one({"username": usr})
            if not user:
                print(Fore.RED, "User not found.")
                print(Style.RESET_ALL)
            if user:
                user = Database.collection.find_one({"username": usr})
                balance = user['bank']
                removeMoney = int(input("Money <-> "))
                money = balance - removeMoney
                filter = {"username": usr}
                newvalues = {"$set": {'bank': money}}
                Database.collection.update_one(filter, newvalues)

        elif command == "addmoney":
            usr = input("user <-> ")
            user = Database.collection.find_one({"username": usr})
            if not user:
                print(Fore.RED, "User not found.")
                print(Style.RESET_ALL)
            if user:
                user = Database.collection.find_one({"username": usr})
                balance = user['bank']
                addMoney = int(input("Money <-> "))
                money = addMoney + balance
                filter = {"username": usr}
                newvalues = {"$set": {'bank': money}}
                Database.collection.update_one(filter, newvalues)

        elif command == "setmoney":
            usr = input("user <-> ")
            user = Database.collection.find_one({"username": usr})
            if not user:
                print(Fore.RED, "User not found.")
                print(Style.RESET_ALL)
            if user:
                user = Database.collection.find_one({"username": usr})
                SetMoney = int(input("Money <-> "))
                filter = {"username": usr}
                newvalues = {"$set": {'bank': SetMoney}}
                Database.collection.update_one(filter, newvalues)

        elif command == "deleteuser":
            usr = input("user <-> ")
            user = Database.collection.find_one({"username": usr})
            if not user:
                print(Fore.RED, "User not found.")
                print(Style.RESET_ALL)
            if user:
                Database.collection.delete_one({"username": usr})
        else:
            print(Fore.RED, "The command not valid.")
            print(Style.RESET_ALL)


def login():
    username = input("username <-> ")
    password = getpass.getpass("password <-> ")
    user = Database.collection.find_one(
        {"username": username, "password": hashlib.sha256(password.encode()).hexdigest()})
    if not user:
        print(Fore.RED, "User not found")
        print(Style.RESET_ALL)
    else:
        if user['admin'] == "True":
            admin()
            exit()
        if user:
            print(Fore.GREEN, "Successfully logged in")
            print(Style.RESET_ALL)

            def user():
                while True:
                    user = Database.collection.find_one(
                        {"username": username, "password": password})
                    commands = ["quit", "balance", "cash",
                                "deposit", "withdraw", "currency", "transfer"]
                    print(Fore.YELLOW, commands)
                    print(Style.RESET_ALL)
                    command = input("command <-> ").lower()

                    if command == "quit":
                        return

                    elif command == "balance":
                        user = Database.collection.find_one(
                            {"username": username, "password": password})
                        print(user['bank'])

                    elif command == "cash":
                        user = Database.collection.find_one(
                            {"username": username, "password": password})
                        print(user['cash'])

                    elif command == "deposit":
                        main = Database.collection.find_one(
                            {"username": username, "password": password})
                        if main:
                            balance = main['bank']
                            _cash = main['cash']
                            amount = int(input("Money <-> "))
                            if _cash < 0:
                                print(
                                    Fore.RED, f"You can't deposit that amount of money you have {_cash} in your wallet.")
                                print(Style.RESET_ALL)
                            else:
                              filter = {"username": username,
                                        "password": password}
                              newvalues = {"$set": {'cash': _cash - amount}}
                              Database.collection.update_one(filter, newvalues)
                              money = amount + balance
                              filter = {"username": username}
                              newvalues = {"$set": {'bank': money}}
                              Database.collection.update_one(filter, newvalues)
                              print(Fore.GREEN, "successfully withdraw the money.")
                              print(Style.RESET_ALL)

                    elif command == "withdraw":
                        main = Database.collection.find_one(
                            {"username": username, "password": password})
                        if main:
                            balance = main['bank']
                            _cash = main['cash']
                            amount = int(input("Money <-> "))
                            if balance < -5000:
                                print(
                                    Fore.RED, f"You can't withdraw that amount of money you have {balance} in your bank.")
                                print(Style.RESET_ALL)
                            else:
                                filter = {"username": username,
                                          "password": password}
                                newvalues = {
                                    "$set": {'bank': balance - amount}, "$set": {'cash': _cash + amount}}
                                Database.collection.update_one(
                                    filter, newvalues)
                                print(Fore.GREEN,
                                      "successfully withdraw the money.")
                                print(Style.RESET_ALL)

                    elif command == "transfer":
                        usr = input("user <-> ")
                        user = Database.collection.find_one({"username": usr})
                        main = Database.collection.find_one(
                            {"username": username, "password": password})
                        if not user:
                            print(Fore.RED, "User not found.")
                            print(Style.RESET_ALL)
                        if user:
                            balance = main['bank']
                            balance2 = user['bank']
                            amount = int(input("Money <-> "))
                            if balance < -5000:
                                print(
                                    Fore.RED, f"You cant Send money you have {balance} in your bank.")
                                print(Style.RESET_ALL)
                            else:
                                filter = {"username": usr}
                                newvalues = {
                                    "$set": {'bank': balance2 + amount}}
                                Database.collection.update_one(
                                    filter, newvalues)
                                filter = {"username": username,
                                          "password": password}
                                newvalues = {
                                    "$set": {'bank': balance - amount}}
                                Database.collection.update_one(
                                    filter, newvalues)
                                print(Fore.GREEN, "Money sent successfully.")
                                print(Style.RESET_ALL)
            user()


def register():
    if contract() == "n":
        print(Fore.RED, "Denied.")
    if contract() == "y":
        print(Fore.GREEN, "Welcome to [Shon Bank] !")
        time.sleep(2)
        print(Style.RESET_ALL)
        os.system("clear")
        username = input("username <-> ")
        password = getpass.getpass("password <-> ")
        if len(password) < 8:
            os.system("clear")
            print(Fore.LIGHTRED_EX,
                  "The password has to be 8 or more length Try again!")
            print(Style.RESET_ALL)
            os.system("clear")
            register()
        string_password = password
        encoded_password = string_password.encode()
        hashed_password = hashlib.sha256(encoded_password).hexdigest()

        user = Database.collection.find_one({"username": username})
        secret = input(
            "Hey, you need to make a secret (Min of 2 characters).")
        if len(secret) < 2:
            os.system("clear")
            print(Fore.LIGHTRED_EX,
                  "The secret has to be 2 or more length Try again.")
            print(Style.RESET_ALL)
            os.system("clear")
            register()
        if user:
            print(Fore.RED, "Username not available.\nPlease try again.")
            print(Style.RESET_ALL)
            register()
        else:
            os.system("clear")
            Database.collection.insert_one({'username': username, 'password': hashed_password,
                                           'bank': 0, 'cash': 5000, 'secret_word': secret, 'admin': "False"})
            print(Fore.LIGHTGREEN_EX, "User Registered.")
            print(Style.RESET_ALL)


def reset():
    secret_word = input("Enter your account Secret Key.")
    usr = input("user <-> ")
    usr2 = Database.collection.find_one({"username": usr})
    if usr2['secret_word'] == secret_word:
        password = getpass.getpass('Enter the new password:')
        if len(password) < 8:
            os.system("clear")
            print(Fore.LIGHTRED_EX,
                  "The password has to be 8 or more length Try again.")
            print(Style.RESET_ALL)
            reset()
        filter = {"username": usr}
        newvalues = {"$set": {'password': password}}
        Database.collection.update_one(filter, newvalues)
    else:
        print(Fore.LIGHTRED_EX, "The secret you mention not valid\nTry again.")
        print(Style.RESET_ALL)
        os.system("clear")
        reset()


if __name__ == "__main__":
    menu()
    char = getch()

    if char == "1":
        register()
    if char == "2":
        login()
    if char == "3":
        reset()
