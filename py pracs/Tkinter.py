from tkinter import *

window=Tk()
window.geometry('500x500')
window.title("form")

fn=StringVar()
ln=StringVar()


def print1():
    print("demo tkinter")
    fName=fn.get()
    lName=ln.get()
    print(fName)
    print(lName)

def exit1():
    exit()

label1=Label(window,text='registration form',fg='blue',width=20,bg='black',relief='solid',font=('arial',16,'bold'))
label1.place(x=90,y=53)

label2=Label(window,text='First name',fg='blue',width=20,font=('arial',10,'bold'))
label2.place(x=80,y=130)

label3=Label(window,text='Last name',fg='blue',width=20,font=('arial',10,'bold'))
label3.place(x=80,y=180)

b1=Button(window,text="login",width=12,bg='brown',command=print1)
b1.place(x=150,y=380)

b2=Button(window,text="Exit",width=12,bg='brown',command=exit1)
b2.place(x=280,y=380)

entry1=Entry(window,textvar=fn)
entry1.place(x=240,y=130)
entry2=Entry(window,textvar=ln)
entry2.place(x=240,y=180)

window.mainloop()