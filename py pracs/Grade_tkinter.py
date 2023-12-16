from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Grade Calculator")

def Calc():
    mark1=int(m1entry.get())
    mark2=int(m2entry.get())
    mark3=int(m3entry.get())
    mark4=int(m4entry.get())
    final=(mark1+mark2+mark3+mark4)/4
    if(final>90):
        result.config(text=f"Excellent {final}")
    elif(final>80 and final<90):
        result.config(text="Good")
    elif(final>70 and final<80):
        result.config(text="Improve")
    elif(final>60 and final<70):
        result.config(text="Fail")
    else:
        result.config(text="Chod")


        
m1=Label(root,text="Marks of Subject 1")
m1.place(x=80,y=50)
m2=Label(root,text="Marks of Subject 2")
m2.place(x=80,y=90)
m3=Label(root,text="Marks of Subject 3")
m3.place(x=80,y=130)
m4=Label(root,text="Marks of Subject 4")
m4.place(x=80,y=170)

m1entry=Entry(root)
m1entry.place(x=300,y=50)
m2entry=Entry(root)
m2entry.place(x=300,y=90)
m3entry=Entry(root)
m3entry.place(x=300,y=130)
m4entry=Entry(root)
m4entry.place(x=300,y=170)

subBut=Button(root,text="Submit",command=Calc)
subBut.place(x=230,y=250)

result=Label(root,text="")
result.place(x=235,y=300)




root.mainloop()
