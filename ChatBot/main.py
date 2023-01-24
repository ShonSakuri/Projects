all = {"hi": "Hello!",
    "how are you": "I'm good, thanks for asking!",
    "bye": "Goodbye!"}

def chat():
    UserInput = input()
    if UserInput in all:
        print(all[UserInput])
    else:
        print("i dont have this word in my dictionery")
chat()