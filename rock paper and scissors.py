from tkinter import *
import random
root=Tk()
root.geometry("500x500")
root.title("ROCK PAPER AND SCISSOR")
root.config(bg='seashell3')
Label(root, text='Rock Paper and Scissors', font='arial 20 bold', bg='seashell2').pack()
user_enter=StringVar()
Label(root, text="Choose rock, paper, scissors", font='arial 20 bold', bg='seashell2').place(x=20, y=70)
Entry(root, text=user_enter, font='arial 20 bold', bg='seashell2').place(x=90, y=130)
computer=random.randint(1, 3)
print(computer)
if computer==1:
    computer='rock'
elif computer==2:
    computer='paper'
else:
    computer='scissors'
rsu=StringVar()
def play():
    user_pick = user_enter.get()
    if user_pick == computer:
        rsu.set('tie,you both select same')
    elif user_pick == 'rock' and computer == 'paper':
        rsu.set('you loose,computer select paper')
    elif user_pick == 'rock' and computer == 'scissors':
        rsu.set('you win,computer select scissors')
    elif user_pick == 'paper' and computer == 'scissors':
        rsu.set('you loose,computer select scissors')
    elif user_pick == 'paper' and computer == 'rock':
        rsu.set('you win,computer select rock')
    elif user_pick == 'scissors' and computer == 'rock':
        rsu.set('you loose,computer select rock')
    elif user_pick== 'scissors' and computer == 'paper':
        rsu.set('you win ,computer select paper')
    else:
        rsu.set('invalid: choose any one -- rock, paper, scissors')
def Reset():
    rsu.set("")
    user_enter.set("")
def Exit():
    root.destroy()


Entry(root, font='arial 10 bold', textvariable=rsu, bg='antiquewhite2', width=50,).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

root.mainloop()