# MAKING A FORM FOR INFO GATHERING....
# VARIABLE CLASSES IN TKINTER == BooleanValu,StringValue,IntVar,DoubleVar....

from tkinter import *
root = Tk()
root.geometry("600x444")
root.title("Creating Form :")

name = Label(root, text="Enter name", pady=10, padx=10)
username = Label(root, text="username", pady=10, padx=10)
password = Label(root, text="passwprd", pady=10, padx=10)
mobile = Label(root, text="mobile-no", pady=10, padx=10)

name.grid()
username.grid(row=1)
password.grid(row=2)
mobile.grid(row=3)

namevalue = StringVar()
usernamevalue = StringVar()
passwordvalue = StringVar()
mobilevalue = StringVar()

nameentry = Entry(root, textvariable=namevalue)
usernameentry = Entry(root, textvariable=usernamevalue)
passwordentry = Entry(root, textvariable=passwordvalue)
mobileentry = Entry(root, textvariable=mobilevalue)

nameentry.grid(row=0, column=1)
usernameentry.grid(row=1, column=1)
passwordentry.grid(row=2, column=1)
mobileentry.grid(row=3, column=1)

b1 = Button(root, text="Submit", bg="yellow", borderwidth=10).grid()

root.mainloop()
