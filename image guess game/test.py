import tkinter
from tkinter import *
import random



question = [
    "THIS IS SAMPLE QUESTIONS 1",
    "THIS IS SAMPLE QUESTIONS 2",
    "THIS IS SAMPLE QUESTIONS 3",
    "THIS IS SAMPLE QUESTIONS 4",
    "THIS IS SAMPLE QUESTIONS 5",
    "THIS IS SAMPLE QUESTIONS 6",
    "THIS IS SAMPLE QUESTIONS 7",
    "THIS IS SAMPLE QUESTIONS 8",
    "THIS IS SAMPLE QUESTIONS 9",
    "THIS IS SAMPLE QUESTIONS 10",
]

answers_choice = [
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"],
    ["1","2","3","4"]
]
answers = [1,1,1,1,1,1,1,1,1,1]
user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x=random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
def showresult(score):
    lbquest.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage=Label(root,background="#ffffff")
    labelimage.pack(pady=(90,0))
    labelresulttext=Label(root, font=("consolas",30),)
    labelresulttext.pack(pady=(50,0))
    if score >= 20:
        img=PhotoImage(file="medal.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text='CONGRATULATIONS!!!! YOU MADE IT',background="#ffffff")
    else:
        img = PhotoImage(file="sad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text='BETTER LUCK TRY NEXT TIME!!', background="#ffffff")




def calc():
    global indexes,user_answer,answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x]==answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques=1
def selected():
    global radvar,user_answer
    global lbquest,r1,r2,r3,r4
    global ques
    x= radvar.get()
    user_answer.append(x)
    radvar.set(-1)
    if ques < 5:
        lbquest.config(text=question[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()

def quiz():
    global lbquest,r1,r2,r3,r4
    lbquest=Label(root,text=question[indexes[0]] , font=("consolas",16),width=500,justify="center",background="#ffffff")
    lbquest.pack(pady=(100,40))

    global radvar

    radvar=IntVar()
    radvar.set(-1)

    r1 = Radiobutton(root, text=answers_choice[indexes[0]][0],font=("Times",20,),value=0,variable=radvar,command=selected,background="#ffffff")
    r1.pack(pady=5)
    r2 = Radiobutton(root, text=answers_choice[indexes[0]][1], font=("Times", 20,), value=1, variable=radvar,command=selected,background="#ffffff")
    r2.pack(pady=5)
    r3 = Radiobutton(root, text=answers_choice[indexes[0]][2], font=("Times", 20,), value=3, variable=radvar,command=selected,background="#ffffff")
    r3.pack(pady=5)
    r4 = Radiobutton(root, text=answers_choice[indexes[0]][3], font=("Times", 20,), value=4, variable=radvar,command=selected,background="#ffffff")
    r4.pack(pady=5)




def start():
    lblimage.destroy()
    lbltext.destroy()
    lblinstruct.destroy()
    lblrule.destroy()
    btn.destroy()
    gen()
    quiz()







root = tkinter.Tk()
root.title("Imagequiz Game")
root.geometry("800x600")
root.config(background="#FFFFFF")

lbltext = Label(root, text="Imagequiz",font = ("Comic sans MS",20,"bold"),background="#ffffff")
lbltext.pack(pady=(0,50))
img2 = PhotoImage(file='play-button (1).png')
btn = Button(root, image=img2,relief=FLAT,border=0,command=start)
btn.pack()
lblinstruct = Label(root, text = "Read the rules of a game \n click on the play button when you are ready to go",background="#ffffff",
                    font = ("Comic sans MS",16,"bold"),justify="center")
lblinstruct.pack(pady=(90,80))

lblrule = Label(root,text="This a Imagequiz Created by Sushant,Samar and Wamsi \n This quiz will contain 5 question \n You will get one chance to select your answers \n All the best for your quiz",width=100,font=("Comic sans MS",10),
                background="#000000",foreground = "yellow",justify="center")
lblrule.pack()

root.mainloop()
