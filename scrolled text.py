from tkinter import *
import tkinter.scrolledtext as tkst
root=Tk()
root.geometry("300x250")
root.title("Scrolled text")
txt=tkst.ScrolledText(root, width=40, height=10)
txt.grid(column=0, row=0)
root.mainloop()