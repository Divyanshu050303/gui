from tkinter import *
root=Tk()
root.geometry("350x520")
root.title("Calculator ")
def click(event):
    global entertext
    text=event.widget.cget("text")
    if text=="=":
        if entertext.get().isdigit():
            value=int(entertext.get())
        else:
            try:
                value=eval(entertext.get())
            except Exception as e:
                value="Error"
        entertext.set(value)
        scre.update()
    elif text=="c":
        entertext.set("")
        scre.update()
    else:
        entertext.set(entertext.get()+text)
        scre.update()


entertext=StringVar()
entertext.set("")
scre=Entry(root, textvar=entertext, font="lucida 40 bold")
scre.pack(fill=X, ipadx=8, padx=10, pady=10)

f=Frame(root, bg="grey")
b=Button(f, text="7", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="8", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="9", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root, bg="grey")
b=Button(f, text="4", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="5", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="6", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root, bg="grey")
b=Button(f, text="1", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="2", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="3", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root, bg="grey")
b=Button(f, text="0", padx=29.5, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text=".", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="c", padx=27.4, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

f.pack()
f=Frame(root, bg="grey")
b=Button(f, text="+", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="-", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="*", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()
f=Frame(root, bg="grey")
b=Button(f, text="/", padx=27, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="%", padx=28, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="=", padx=26.4, pady=18)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()