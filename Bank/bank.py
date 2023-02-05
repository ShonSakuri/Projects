import pymongo
import sys
import tty
import time
import os
import termios
from colorama import Fore, Style

client = pymongo.MongoClient("mongodb+srv://shon:SeanSak123@cluster0.wrckk3j.mongodb.net")

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
char = getch()

print("""
Register - You need to click 1 Key to Register.
Login - You need to click 2 Key to Login.
Reset Password - You need to click 3 key to reset your password.
""")

def admin():
      tr = True
      while tr:
            commands = ["removemoney","addmoney","quit","setmoney","deleteuser"]
            print(Fore.YELLOW,commands)
            print(Style.RESET_ALL)
            time.sleep(3)
            command = input("command <-> ").lower()

            if command == "quit":
                  tr = False

            elif command == "removemoney":
                  usr = input("user <-> ")
                  user = collection.find_one({"username": usr})
                  if not user:
                        print(Fore.RED,"User not found.")
                        print(Style.RESET_ALL)
                  if user:
                        user = collection.find_one({"username": usr})
                        balance = user['bank']
                        removeMoney = int(input("Money <-> "))
                        money = balance - removeMoney
                        filter = {"username": usr}
                        newvalues = {"$set": {'bank': money} }
                        collection.update_one(filter, newvalues)

            elif command == "addmoney":
                  usr = input("user <-> ")
                  user = collection.find_one({"username": usr})
                  if not user:
                        print(Fore.RED,"User not found.")
                        print(Style.RESET_ALL)
                  if user:
                        user = collection.find_one({"username": usr})
                        balance = user['bank']
                        addMoney = int(input("Money <-> "))
                        money = addMoney + balance
                        filter = {"username": usr}
                        newvalues = {"$set": {'bank': money} }
                        collection.update_one(filter, newvalues)

            elif command == "setmoney":
                  usr = input("user <-> ")
                  user = collection.find_one({"username": usr})
                  if not user:
                        print(Fore.RED,"User not found.")
                        print(Style.RESET_ALL)
                  if user:
                        user = collection.find_one({"username": usr})
                        SetMoney = int(input("Money <-> "))
                        filter = {"username": usr}
                        newvalues = {"$set": {'bank': SetMoney} }
                        collection.update_one(filter, newvalues)
            
            elif command == "deleteuser":
                  usr = input("user <-> ")
                  user = collection.find_one({"username": usr})
                  if not user:
                        print(Fore.RED,"User not found.")
                        print(Style.RESET_ALL)
                  if user:
                        collection.delete_one({"username": usr})
            else:
                  print(Fore.RED,"The command not valid.")
                  print(Style.RESET_ALL)
                  
def login():
      username = input("username <-> ")
      password = input("password <-> ")
      user = collection.find_one({"username": username, "password": password})
      os.system("clear")

      if not user:
            print(Fore.RED,"User not found")
            print(Style.RESET_ALL)
      else:
            user = collection.find_one({"username": username, "password": password})
            if user['admin'] == "True":
                  admin()
                  exit()
            if user:
                  print(Fore.GREEN,"Successfully logged in")
                  print(Style.RESET_ALL)
                  time.sleep(2)
                  def user():
                        rr = True
                        while rr:
                              user = collection.find_one({"username": username, "password": password})
                              commands = ["quit","balance","sendmoney"]
                              print(Fore.YELLOW,commands)
                              print(Style.RESET_ALL)
                              time.sleep(3)
                              command = input("command <-> ").lower()
                              
                              if command == "quit":
                                    rr = False

                              elif command == "balance":
                                    user = collection.find_one({"username": username, "password": password})
                                    print(user['bank'])

                              elif command == "sendmoney":
                                    usr = input("user <-> ")
                                    user = collection.find_one({"username": usr})
                                    main = collection.find_one({"username": username, "password": password})
                                    if not user:
                                          print(Fore.RED,"User not found.")
                                          print(Style.RESET_ALL)
                                    if user:
                                      balance = main['bank']
                                      balance2 = user['bank']
                                      amount = int(input("Money <-> "))
                                      if amount > balance:
                                        print(Fore.RED,"You don't have enough money in your balance.")
                                        print(Style.RESET_ALL)
                                      else:
                                        filter = {"username": usr}
                                        newvalues = {"$set": {'bank': balance2 + amount} }
                                        collection.update_one(filter, newvalues)
                                        filter = {"username": username, "password": password}
                                        newvalues = {"$set": {'bank': balance - amount} }
                                        collection.update_one(filter, newvalues)
                                        print(Fore.GREEN,"Money sent successfully.")
                                        print(Style.RESET_ALL)
                  user()

def register():
      username = input("username <-> ")
      password = input("password <-> ")
      user = collection.find_one({"username": username})
      secret = input("Enter your secret word.\ncan be your Dog name or maybe your nickname.\nYou have to remember it after you write it (Min of 2 characters).")
      if len(secret) < 2:
            os.system("clear")
            print(Fore.LIGHTRED_EX,"The secret has to be 2 or more length Try again.")
            print(Style.RESET_ALL)
            register()
      if user:
            os.system("clear")
            print(Fore.RED,"Username not available.\nPlease try again.")
            print(Style.RESET_ALL)
            register()
      else:
            if len(password) < 8:
                  os.system("clear")
                  print(Fore.LIGHTRED_EX,"The password has to be 8 or more length Try again.")
                  print(Style.RESET_ALL)
                  register()
            collection.insert_one({'username': username, 'password': password, 'bank': 0,'secret_word': secret, 'admin': "False"})
            print(Fore.LIGHTGREEN_EX,"User Registered.")
            print(Style.RESET_ALL)

def reset():
      secret_word = input("Enter your account Secret Key.")
      usr = input("user <-> ")
      if usr['secret_word'] == secret_word:
            password = input("Enter the new password.")
            if len(password) < 8:
                  os.system("clear")
                  print(Fore.LIGHTRED_EX,"The password has to be 8 or more length Try again.")
                  print(Style.RESET_ALL)
                  reset()
            filter = {"username": usr}
            newvalues = {"$set": {'password': password} }
            collection.update_one(filter, newvalues)
      else:
            print(Fore.LIGHTRED_EX,"The secret you mention not valid\nTry again.")
            print(Style.RESET_ALL)
            reset()

if char == "1":
      register()
if char == "2":
      login()
if char == "3":
      reset()