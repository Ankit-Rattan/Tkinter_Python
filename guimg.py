from tkinter import *
from PIL import Image, ImageTk
# Default tkinter PhotoImage does NOT allow jpg image access, to access such image, use PIL (i.e pillow)

root = Tk()

root.geometry("500x400")

# for png images (default)
# pic = PhotoImage(file="sample.png") 

# From JPG images : 
img = Image.open("sample1.jpg")
pic = ImageTk.PhotoImage(img)
 

labpic = Label(image=pic)
labpic.pack()

root.mainloop()