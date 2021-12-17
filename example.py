from tkinter import *
root = Tk()
root.geometry("980x434")
root.title("Frame Making!")

frame1 = Frame(root, bg="blue", borderwidth=10, relief=SUNKEN)
frame1.pack(side=LEFT, fill="y")

lb1 = Label(frame1, text="Welcome!", font="monospace 8 bold")
lb1.pack(pady=42)

frame2 = Frame(root, bg="red", borderwidth=5, relief=SUNKEN)
frame2.pack(side=BOTTOM, fill="x")

lb2 = Label(frame2, text="BabyBoy!", font="sansserif 10 bold")
lb2.pack(pady=50, padx=50)

frame3 = Frame(root, bg="blue", borderwidth=5, relief=SUNKEN)
frame3.pack(side=TOP, fill="x")

lb3 = Label(frame3, text="CongoTai!", bg="black",
            fg="white", font="Helvetica 8 bold")
lb3.pack(pady=50, padx=50)
root.mainloop()
