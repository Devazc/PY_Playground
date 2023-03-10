#A Password Generator with TKINTERT

#IMPORTING LIBRARIES
import tkinter
from tkinter import *
import random, string
import pyperclip

#INTIALIZING WINDOW
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.configure(background='Black')
root.title("PASSWORD GENERATOR")

Label(root, text = "PASSWORD GENERATOR",font = "arial 15 bold").pack()

#SELECT PASSWORD LENGTH
pass_label = Label(root, text ='PASSWORD LENGTH',font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width=15).pack()

#Function to generate Variable

pass_str = StringVar()

def Generator():
    password = ' '

    for x in range(0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)

        for y in range(pass_len.get()-4):
            password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    pass_str.set(password)     

Button(root, text = 'GENERATE PASSWORD', command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

#Function Copy Password

def Copy_Password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'Copy to Clipboard', command=Copy_Password).pack(pady=5)


root.mainloop()

