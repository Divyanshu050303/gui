import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar
root=tk.Tk()
root.geometry("300x250")
root.title("Progress bar")
style=ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')
p=Progressbar(root, length=180, style='black.Horizontal.TProgressbar')
p["value"]=50
p.grid(column=0, row=0)
root.mainloop()