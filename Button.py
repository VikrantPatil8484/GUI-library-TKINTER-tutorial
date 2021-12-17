# MAKING BUTTONS *** Command=text is used to print what we wznt after clicking pn button

from tkinter import *
root = Tk()
root.geometry("800x434")
root.title("Making Buttons!")


def hello():
    print("Hello Vicky!")


def name():
    print("Hello Vickudi! ")


f1 = Frame(root, bg="red", borderwidth=15, relief=GROOVE)
f1.pack(side=LEFT, anchor="sw")

b1 = Button(f1, text="Baby-Boy", bg="grey", command=hello)
b1.pack(side=LEFT, padx=20)

b2 = Button(f1, text="ClickMe", bg="grey", command=name)
b2.pack(side=LEFT, padx=10)


b3 = Button(f1, text="Congo!", bg="grey")
b3.pack(side=LEFT, padx=30)

root.mainloop()
