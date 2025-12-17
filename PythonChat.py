import random as rand
import os
import string

# Sub to GamerJig!

history = []
chathistory = []

def random_id(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(rand.choices(characters, k=length))

def clear():
    os.system("cls")

delete = None
what = ""
running = False
admin = False
sending = True
clear()
user = str(input("Enter a username: "))

if user.lower() == "gamerjig":
    admin = True

running = True

while running == True:
    if admin == True:
        what = str(input("Delete or Send message? "))
        clear()
        for i in chathistory:
            print(">", i)
    
    if what.lower() == "send":
        sending = True
    else:
        sending = False
        Gamerjig = True
    
    if admin == False:
        sending = True

    if sending == True:
        id = random_id(8)
        message = str(input("- "))

        history.append({"user": user, "message": message, "id": id})
        chathistory.append(message)
        clear()
        for i in chathistory:
            print(">", i)

    if sending == False and admin == True:
        delete = str(input("Deleting: "))
        for i in range(len(chathistory)-1, -1, -1):
            if chathistory[i] == delete:
                chathistory.pop(i)
        clear()
        for i in chathistory:
            print(">", i)