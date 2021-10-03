#!/usr/bin/env python
# coding: utf-8

# In[95]:


from tkinter import*
from datetime import date
import tkinter.messagebox as msg

root=Tk()

root.geometry("650x650")
root.resizable(False,False)
root.title("Age Calculator")

name=PhotoImage(file='C:\\age_calc.png')
image=Label(image=name).pack(padx=15,pady=56)

def calculateAge():
    today=date.today()
    birthDate=date(int(yearTextBox.get()),int(monthTextBox.get()),int(dayTextBox.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    output= msg.showinfo("Age Calculator",f"Name: {nameValue.get()}\nAge: {age} Years Old")
                 
Label(text="Name: ").place(x=190,y=250)
Label(text="Year:").place(x=190,y=300)
Label(text="Month:").place(x=190,y=350)
Label(text="Day:").place(x=190,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameTextBox=Entry(root, textvariable=nameValue,width=30,bd=3)
nameTextBox.place(x=240,y=250)

yearTextBox=Entry(root, textvariable=yearValue,width=30,bd=3)
yearTextBox.place(x=240,y=300)

monthTextBox=Entry(root, textvariable=monthValue,width=30,bd=3)
monthTextBox.place(x=240,y=350)

dayTextBox=Entry(root, textvariable=dayValue,width=30,bd=3)
dayTextBox.place(x=240,y=400)

submit= Button(root,text="Submit",command=calculateAge)
submit.place(x=300,y=450)

root.mainloop()


# In[ ]:



Label(text=f"Name: {nameValue.get()}\n\nAge: {age} Years Old").place(x=500,y=300)

