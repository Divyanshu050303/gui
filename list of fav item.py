from tkinter import *
root=Tk()
root.geometry("300x250")
root.title("List of favourite language")
l1=Label(root, text="List of favourite language")
listbox=Listbox(root)
listbox.insert(1, "PHP")
listbox.insert(2, "Python")
listbox.insert(3, "Java")
listbox.insert(4, "C#")
l1.pack()
listbox.pack()
root.mainloop()