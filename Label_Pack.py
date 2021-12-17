# Label And Pack Attributes are as follow ----LABEL - (text=adds text)
# bg = background
# fg = foreground
# font = sets font family
# padx = x padding horizontally
# pady = y padding vertically
# relief = border styling :SUNKEN,GROOVE,etc.
# PACK attributes :
# fill = None, X(horizontally), Y(vertically), Both(hori + vertical)
# Side = placing BOTTOM, TOP, LEFT, RIGHT..
# Anchor = Text positioned north,west,south,east ---- ne,nw,sw,se.

from tkinter import *
root = Tk()

root.geometry("1000x434")  # witdh / height

root.title("WELCOME TO TKINTER PARADISE!")

Patil = Label(text="Hello Folks!\n Myself Vikrant Patil an enthusiatstic Software Engineer\n Dreaming to get placement in \n @FACEBOOK\n@GOOGLE\n@AMAZON\n@MICROSOFT",
              bg="green", fg="white", padx=20, pady=25, font="fantasy 5 bold", borderwidth=5, relief=RIDGE)

Patil.pack(side=TOP, anchor="sw", fill=X)

root.mainloop()
