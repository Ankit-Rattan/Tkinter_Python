from tkinter import *

root = Tk()
canvas_h = 400
canvas_w = 500
root.geometry(f"{canvas_w}x{canvas_h}")
can_widget = Canvas(root, width=canvas_w, height=canvas_h)
can_widget.pack()

# Line goes from x1, y1 to x2, y2
can_widget.create_line(0, 0, 500, 400, fill="red", width=2)
can_widget.create_rectangle(100, 100, 300, 300, fill="orange", width=2)

can_widget.create_oval(100, 100, 400, 300, fill="yellow", width=2)


root.mainloop()