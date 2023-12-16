from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("Registartion form")

def Print():
    print("Demo")

def exit1():
    exit()

fn=StringVar()
ln=StringVar()

label1=Label(window,text="Registartion Form",relief="solid",width=20,font=("arial",16,"bold"))
label1.place(x=90,y=53)        

label2=Label(window,text='First name',fg='blue',width=20,font=('arial',10,'bold'))
label2.place(x=80,y=130)

entry1=Entry(window,textvar=fn)
entry1.place(x=240,y=242)
entry2=Entry(window,textvar=ln)
entry2.place(x=240,y=282)

label3=Label(window,text='Last name',fg='blue',width=20,font=('arial',10,'bold'))
label3.place(x=80,y=180)

b1=Button(window,text="login",width=12,bg='brown',command=Print)
b1.place(x=150,y=380)

b2=Button(window,text="Exit",width=12,bg='brown',command=exit1)
b2.place(x=280,y=380)
