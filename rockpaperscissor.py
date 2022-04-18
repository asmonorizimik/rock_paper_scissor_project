from tkinter import *
from PIL import Image, ImageTk
from random import randint
root = Tk()
root.title("rock paper and scissor")
root.configure(background="pink")

image_rock1=ImageTk.PhotoImage(Image.open("rock.png"))
image_paper1=ImageTk.PhotoImage(Image.open("paper.png"))
image_scissor1=ImageTk.PhotoImage(Image.open("scissor.png"))

image_rock2=ImageTk.PhotoImage(Image.open("user_rock.png"))
image_paper2=ImageTk.PhotoImage(Image.open("user_paper.png"))
image_scissor2=ImageTk.PhotoImage(Image.open("user_scissorr.png"))

label_player=Label(root,image=image_rock1)
label_computer=Label(root,image=image_rock2)
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score=Label(root,text=0,font=("arial",60,"bold"),fg="red")
player_score=Label(root,text=0,font=("arial",60,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

player_indi=Label(root,font=("arail",40,"bold"),
                text="PLAYER",bg="orange",fg="blue")
computer_indi=Label(root,font=("arial",40,"bold"),
                       text="COMPUTER",bg="green",fg="blue" )
computer_indi.grid(row=0,column=1)
player_indi.grid(row=0,column=3)

def msg_updation(a):
    final['text']=a

def computer_update():
    final= int(computer_score['text'])
    final+=1
    computer_score['text']=str(final)
def player_update():
    final= int(player_score['text'])
    final+=1
    player_score['text']=str(final)


def winner_check(p,c):
    if p==c:
        msg_updation("It's a tie")
    elif p=="rock":
        if c=="paper":
            msg_updation("computer win")
            computer_update()
        else:
            msg_updation("player wins")
            player_update()
    elif p=="paper":
        if c=="scissor":
            msg_updation("computer wins")
            computer_update()
        else:
            msg_updation("player win")
            player_update()
    elif p=="scissor":
        if c=="rock":
            msg_updation("computer win")
            computer_update()
        else:
            msg_updation("player win")
            player_update()
    else:
        pass
to_select=["rock","paper","scissor"]
def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer=="rock":
        image_names.configure(image=image_rock2)
    elif choice_computer=="paper":
        image_names.configure(image=image_paper2)
    else:
        image_names.configure(image=image_scissor2)


    if a=="rock":
        img_player.configure(image=image_rock1)
    elif a=="paper":
        img_player.configure(image=image_paper1)
    else:
        img_player.configure(image=image_scissor1)

    winner_check(a,choice_computer)

final=Label(root,font=("arial",40,"bold"),bg="red",fg="white")
final.grid(row=3,column=2)


button_rock=Button(root,width=16,height=3,
                    text="ROCK",font=("arail",20,"bold"),bg="yellow",fg="black",).grid(row=2,column=1)
button_paper=Button(root,width=16,height=3,text="PAPER",
                    font=("arial",20,"bold"),bg="yellow",fg="red").grid(row=2,column=2)
button_scissor=Button(root,width=16,height=3,text="SCISSOR",
                    font=("arial",20,"bold"),bg="yellow",fg="red").grid(row=2,column=3)




root.mainloop()