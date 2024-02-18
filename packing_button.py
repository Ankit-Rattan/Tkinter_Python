from tkinter import *

root = Tk()
root.geometry("500x400")

def printme():
    print("Hello ankit")

f1 = Frame(root, bg="grey", relief="sunken", borderwidth=5)
f1.pack(side="top", fill="y")

b1 = Button(f1, text="Click Me", font="bold", command=printme)
b1.pack(padx="10", pady="10", side="left")
b2 = Button(f1, text="Click Me", font="bold")
b2.pack(padx="10", pady="10", side="left")
root.mainloop()