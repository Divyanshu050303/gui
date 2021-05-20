from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("SPINBOX")
m=DoubleVar()
spin_box=Spinbox(root, from_=0.6,  to=50.0, increment=0.1, textvariable=m)
spin_box.pack()
root.mainloop()