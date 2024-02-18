from tkinter import *  

root = Tk()  # creates a basic gui

# GUI Logic 

root.geometry("500x400") #-> geometry("width x height") : it decides the hieght and witdh

# minsize(width, height)
root.minsize(200, 200)
# maxsize(width, height)
root.maxsize(700, 700)

# Label : It is a widget that user DOES NOT interact with.

lab = Label(text="Hello ankit here", bg="black", fg="white", font="bold")
lab.pack() #-> pack() is used to display the widget in the window. If you will not use then it will not display it.

root.mainloop()   #-> it keeps running until the user closes the window and remeber the logic of the event for the ui
