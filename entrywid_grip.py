from tkinter import *

def getVal():
    print(uservalue.get())	

root = Tk()
root.geometry("500x400")

user = Label(root, text="Username")
password = Label(root, text="password")
# Packing with the help of .grid
user.grid(row=0, column=0)  # by defualt grid is set to row=0 , coloumn=0
password.grid(row=1, column=0)

# Variable classes in tkinter => BooleanVar, StringVar, IntVar , DoubleVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getVal).grid(row=2, column=1)	

root.mainloop()