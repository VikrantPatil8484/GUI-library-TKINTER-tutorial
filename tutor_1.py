# starting Making GUI - first import tkinter module by writing following
# making basic GUI Root😍

from tkinter import *
vicks_gui_root = Tk()

# Its always WIDTH / HEIGHT remember..
vicks_gui_root.geometry("644x434")

vicks_gui_root.minsize(200, 100)

vicks_gui_root.maxsize(1200, 988)

# Label is Widget where user do not interact.
vickudi = Label(text="Let's Rock!")

# We must have to Pack The Label just like after packing cloths into the sootcase we close the sootcase..😂😂😂
vickudi.pack()
vicks_gui_root.mainloop()
