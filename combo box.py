import tkinter.ttk
from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("Combo box")
m=StringVar()
combo=tkinter.ttk.Combobox(root, textvariable=m, value=["python", "tkinter", "divyanshu"])
combo.pack()
root.mainloop()