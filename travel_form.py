from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("Travel Form")	

def getval():
    print("Submitted Form")
    # print(f"{nameval.get(), phoneval.get(), genderval .get(), modeval.get(), foodserval.get()}")
    with open("travel_form.txt", "a") as f:
        f.write(f"{nameval.get(), phoneval.get(), genderval.get(), modeval.get(), foodserval.get()}\n")

Label(root, text="Treavel Form", font="bold", pady=15).grid(row=0, column=4)

name = Label(root, text="Name").grid(row=1, column=1)
phone = Label(root, text="Phone").grid(row=2, column=1)
gender = Label(root, text="Gender").grid(row=3, column=1)
mode = Label(root, text="Payment Mode").grid(row=4, column=1)


# Variable for storing value
nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
modeval = StringVar()
foodserval = IntVar() # -> checkbox


# Entries for the form + packing via grid
nameentry = Entry(root, textvariable=nameval).grid(row=1, column=2)
phoneentry = Entry(root, textvariable=phoneval).grid(row=2, column=2)
genderentry = Entry(root, textvariable=genderval).grid(row=3, column=2)
modeentry = Entry(root, textvariable=modeval).grid(row=4, column=2)

# Checkbox + packing via grid
foodser = Checkbutton(root, text="Food Servies", variable=foodserval).grid(row=5, column=2)

Button(root, text="Submit", command=getval).grid(row=6, column=2)

root.mainloop()