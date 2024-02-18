from tkinter import *

def eventcall(event):
    print(event)

root = Tk()
root.geometry("500x400")

widget = Button(root, text="Click Me", font="bold")
widget.pack()

# There are many event format : Refer documentation

widget.bind("<Button-1>", eventcall)
widget.bind("<Double-1>", quit)

root.mainloop()