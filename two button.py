from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("TWO BUTTON")
b1=Button(root, text="Hello", width=20, height=5, bg="black", fg="red")
b1.pack(side=LEFT)
b2=Button(root, text="exit", width=40, height=5, bg="black", fg="red")
b2.pack(side=RIGHT)
root.mainloop()