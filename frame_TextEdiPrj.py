from tkinter import *

root = Tk()
root.geometry("500x400")

# Frame
# Frame -> is a widget that is used to group other widgets. (Like div tag in web)
f1 = Frame(root, bg="grey", relief="sunken", borderwidth=5)
f1.pack(side="left", fill="y")

f2 = Frame(root, bg="dark grey", relief="groove", borderwidth=5)
f2.pack(side="top", fill="x")

l = Label(f1, text="Text-Editor", font="bold")
l.pack(padx="10", pady="10")
l1 = Label(f1, text="Folder Name", font="bold")
l1.pack(padx="10" ,pady="10")

l3 = Label(f2, text="Your Text is Here", font="Aerial 15 bold")
l3.pack(padx="10" ,pady="10")

root.mainloop()