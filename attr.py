from tkinter import *
import os

root = Tk()
root.geometry("500x400")

# To get the curretn working dir.
path = os.getcwd()

# Changing the title: 
# It is not must to show dir. path in title.
root.title(path+  " Ankit")


# Important Label Options
'''
text -> text to be displayed
bg or background -> background
fg -> foreground
font -> sets the font
padx -> padding in x axis
pady -> padding in y axis
relief -> border styling => SUNKEN, RAISED, GROOVE, RIDGE, FLAT
'''

title_label = Label(text="dhskdjslf \n dshfsdkjfsfdkafkdjhaifkidsukj\nisdfjsidkjfskfjd", bg="black", fg="white", font="bold", padx=10, pady=50, relief="groove", borderwidth=5)

# Important Pack Options
'''
anchor -> where to place the widget (ex : nw(i.e north-west), es, etc)
side -> where to place the widget (left, right, top, bottom). By default it is top
fill -> to fill the space (x, y, both)
padx -> padding in x axis
pady -> padding in y axis


'''


title_label.pack(anchor="nw", side="top", fill="x", padx=10, pady=50)

root.mainloop()