#IMPORTING MODULES
import tkinter
from tkinter import *
import random





# USING ARRAY FOR STORING QUESTIONS
question = [
    "Which animal was shown in the picture 1 ?",
    "Which animal was Shown in the picture 2 ?",
    "Which animal was shown in the picture 3 ?",
    "Which animal was shown in the Picture 4 ?",
    "Which bird was shown in the picture 5 ?",
    "Which bird was shown in the picture 6 ?",
    "Which object was shown in the picture 7 ?",
    "Which object was shown in the picture 8 ?",
    "Which fruit was shown in the picture 9 ?",
    "Which fruit was shown in the picture 10",
]
# USING ARRAY TO STORE USERS_ANSWERS
answers_choice = [
    ["Cat","Dog","Elephant","Lion"],
    ["Dog","Rat","Lion","Elephant"],
    ["Dog","Cat","Rabbit","Lion"],
    ["Dog","Rabbit","Cat","Lion"],
    ["eagle","Parrot","Pigeon","Vulture"],
    ["eagle","Pigeon","Parrot","Vulture"],
    ["Bat","Ball","Sphere","Stick"],
    ["Pomegranate","Apple","Grapes","Orange"],
    ["Pomegranate","Orange","Grapes","Apple"],
    ["Pomegranate","Grapes","Apple","Orange"],

]
# USING ARRAY TO STORE CORRECT ANSWERS
answers = [1,1,1,1,1,1,1,1,1,1]
user_answer = []# USING ARRAY TO STORE USER ANSWERS

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x=random.randint(0,9)# USING RANDOM MODULE TO GET 5 QUESTIONS RANDOMLY OUT IOF 10
        if x in indexes:
            continue
        else:
            indexes.append(x)
def showresult(score):#USING THIS FUNCTION TO SHOW RESULT OR SCORE
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
        # THIS IS THE CODE FOR GETTING SCORE >=20
        img=PhotoImage(file="med.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text='CONGRATULATIONS!!!! YOU MADE IT \n KEEP IT UP',background="#ffffff")
    else:
        # THIS IS THE LINE OF CODE FOR GETTING SCORE <20
        img = PhotoImage(file="sad (1).png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text='BETTER LUCK TRY NEXT TIME!!', background="#ffffff")




def calc():# THIS FUNCTION IS USED FOR MATCHING ANSWERS AND INCEMENT OF SCORE
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
    radvar.set(-1)# THIS IS USED TO CHANGE THE PRESELECTED RADIOBUTTON
    if ques < 5:
        lbquest.config(text=question[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1# THIS IS USED TO INCREMENT THE COUNTER OF YOUR QUESTION JuST BY SELECTING THE OPTION IT WILL AUTOMATICALLY
        #GO ON THE NEXT QUESTION BECASUE WE HAVE NOT MADE ANY NEXT OR SUBMIT BUTTON
    else:
        calc()

def quiz():
    global lbquest,r1,r2,r3,r4
    lbquest=Label(root,text=question[indexes[0]] , font=("consolas",16),width=500,justify="center",background="#ffffff")
    lbquest.pack(pady=(100,40))

    global radvar

    radvar=IntVar()
    radvar.set(-1)
# R1,R2,R3,R4 ARE THE RADIOBUTTONS WHICH ARE USED AS OPTIONS
    r1 = Radiobutton(root, text=answers_choice[indexes[0]][0],font=("Times",20,),value=0,variable=radvar,command=selected,background="#ffffff")
    r1.pack(pady=5)
    r2 = Radiobutton(root, text=answers_choice[indexes[0]][1], font=("Times", 20,), value=1, variable=radvar,command=selected,background="#ffffff")
    r2.pack(pady=5)
    r3 = Radiobutton(root, text=answers_choice[indexes[0]][2], font=("Times", 20,), value=3, variable=radvar,command=selected,background="#ffffff")
    r3.pack(pady=5)
    r4 = Radiobutton(root, text=answers_choice[indexes[0]][3], font=("Times", 20,), value=4, variable=radvar,command=selected,background="#ffffff")
    r4.pack(pady=5)




def start():# THIS FUNCTION WILL BE CALLED ON PRESSING THE PLAY BUTTON ICON
    lblimage1.destroy()
    lblinstruct.destroy()

    btn.destroy()
    gen()
    quiz()







root = tkinter.Tk()
root.title("Imagequiz Game")
root.iconbitmap(r"Imagequiz.ico")# THIS IS UDED FOR CHANGING THE DEAFUALT FRAME ICON OF TKINTER FROM TK TO "IMAGEQUIZ"
root.geometry("800x600")

root.config(background="#FFFFFF")# "#FFFFFF" IT REPRESENTS THE WHITE COLOUR IN THE FORM OF RGB CODE


img2 = PhotoImage(file='play-button (1).png')
btn = Button(root, image=img2,relief=FLAT,border=0,command=start)
btn.pack()# THIS IS THE PLAYBUTTON OF GAME
# THIS IS THE INSTRUCTIONS OF OUR GAME
lblinstruct = Label(root, text = "See the images shown and memorise them \n Once you done with memorising the picture \n click on the play button ",background="#ffffff",
                    font = ("Comic sans MS",14,"bold"),justify="center")
lblinstruct.pack(pady=(10,0))
img1 = PhotoImage(file='proj1.png')
lblimage1 = Label(root, image=img1,background="#ffffff",justify="center")
lblimage1.pack(pady=(10,0))# THIS IS USED TO DISPLAY THE 10 PICTURES
def Closelabel():
    lblimage1.destroy()

lblimage1.after(30000,Closelabel) # THIS IS USED TO DISPLAY THE 10 PICTURES for 30 seconds OnLy





root.mainloop()
