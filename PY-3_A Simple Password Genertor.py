#A Simple Password Genertor

import string
import random

Length = int(input("Enter the Required Length of the Password: "))

print("Choose character set for the password from the below:\n"\
    "1.Letters\n"\
        "2.Digits\n"\
            "3.Special Characters\n"\
                "4.Exit")

characterlist = ""

while(True):
    choice = int(input("Pick a Number from Above List: "))
    if choice == 1:
        characterlist += string.ascii_letters

    elif choice == 2:
        characterlist += string.digits

    elif choice == 3:
        characterlist += string.punctuation

    elif choice == 4:
        break
    else:
        print("Pick a Valid Option: ")


password = []

for i in range(Length):
    randomchar = random.choice(characterlist)
    password.append(randomchar)
    
password = "".join(password)

X = password.isalpha()
if X == True:
    print("Weak Password")

Y = password.isalnum()
if Y == True:
    print("Easy Password")

else:
    print("Strong Password")


print("The Random Password is: "+ password)



