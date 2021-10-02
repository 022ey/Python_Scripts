#----------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------Student Management System-------------------------------------------------------- #
#----------------------------------------------------------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------Imported Required Modules--------------------------------------------------#

from tkinter import *
import tkinter.messagebox as msg
from PIL import Image,ImageTk
import sqlite3

#----------------------------------------------------------------Main Window--------------------------------------------------#

root=Tk()
root.title("Student Management System")
root.wm_iconbitmap("C:\\gdgs_icon.ico")
root.resizable(0,0)

#----------------------------------------------------------------Database Connection--------------------------------------------------#

def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn    

#----------------------------------------------------------------Value Validation--------------------------------------------------#

def verifier():
    a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=0
    
    if not student_name.get():
        t1.insert(END,"Student name is required\n")
        a=1
    elif student_name.get().isdigit():
        t1.insert(END,"Invalid Student name\n")
        b=1
    if not scholar_number.get():
        t1.insert(END,"Scholar No. is required\n")
        c=1
    elif not scholar_number.get().isdigit():
        t1.insert(END,"Invalid Scholar number\n")
        d=1
    if not stream.get() :
        t1.insert(END,"Stream is required\n")
        e=1
    elif stream.get().isdigit():
        t1.insert(END,"Invalid Stream\n")
        f=1
    if not phone.get():
        t1.insert(END,"Phone number is required\n")
        g=1
    elif not phone.get().isdigit():
        t1.insert(END,"Invalid Phone number\n")
        h=1
    elif not len(str(phone.get())) == 10:
        t1.insert(END, "Invalid Phone number\n")
        i=1
    if not father.get():
        t1.insert(END,"Father name is required\n")
        j=1
    elif father.get().isdigit():
        t1.insert(END,"Invalid Father name\n")
        k=1
    if not mother.get():
        t1.insert(END,"Mother name is required\n")
        l=1
    elif mother.get().isdigit():
        t1.insert(END,"Invalid Mother name\n")
        m=1
    if not address.get():
        t1.insert(END,"Address is Required\n")
        n=1
    elif address.get().isdigit():
        t1.insert(END,"Invalid Address\n")
        o=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 or k==1 or l==1 or m==1 or n==1 or o==1:
        return 1
    else:
        return 0

#----------------------------------------------------------------Created Database and Added Records in The Table --------------------------------------------------#

def add_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,SCHOLAR_NO INTEGER,STREAM TEXT,PHONE_NO INTEGER,FATHER TEXT,MOTHER TEXT,ADDRESS TEXT)")
        cur.execute("insert into STUDENTS values(?,?,?,?,?,?,?)",(str(student_name.get()),str(scholar_number.get()),str(stream.get()),str(phone.get()),str(father.get()),str(mother.get()),str(address.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"ADDED SUCCESSFULLY\n")

#----------------------------------------------------------------Fetching Database To View Student's Record--------------------------------------------------#

def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")
        
#----------------------------------------------------------------Deletion of Particular Student's Record Whenever Required-------------------------------------------------#

def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE SCHOLAR_NO=?",(str(scholar_number.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")

#----------------------------------------------------------------Updation of Particular Student's Record Whenever Required-------------------------------------------------#
        
def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,SCHOLAR_NO=?,STREAM=?,PHONE_NO=?,FATHER=?,MOTHER=?,ADDRESS=? where SCHOLAR_NO=?",(student_name.get(),str(scholar_number.get()),stream.get(),str(phone.get()),father.get(),mother.get(),address.get(),str(scholar_number.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")

#----------------------------------------------------------------To Clear The Text Box-------------------------------------------------#
        
def clear():
    t1.delete(1.0,END)

#----------------------------------------------------------------To Close The GUI-------------------------------------------------#
    
def close():
    root.destroy() 

#----------------------------------------------------------------Shows Project's Info in a Message Box-------------------------------------------------#

def info():
    msg.showinfo("Info","Student Management System for Class 11th and 12th developed by Mohd Akif.")

#----------------------------------------------------------------Shows Feedback of User-------------------------------------------------#

def exp():
    feedback= msg.askquestion("Info","Does this Program helpful to you?")
    if feedback=="yes":
        msg.showinfo("Info","Great! Thank you for using our service.")
        
    else:
        msg.showinfo("Info","Tell us where you lag. We'll fix it soon!")
        
#----------------------------------------------------------------Main Menu and Submenu-------------------------------------------------#
        
menu2=Menu(root)
menu=Menu(menu2,tearoff=0)
menu.add_command(label="Info",command=info)
menu.add_command(label="How was your experience?",command=exp)
menu2.add_cascade(label="Help",menu=menu)
root.config(menu=menu2)

#----------------------------------------------------------------School's Logo in JPG Format-------------------------------------------------#

img=Image.open("C:\\gdgs2.jpg")
photo=ImageTk.PhotoImage(img)

ph=Label(image=photo)
ph.place(x=104,y=10)

#----------------------------------------------------------------School's Campus Photo in JPG Format-------------------------------------------------#

img2=Image.open("C:\\gdgs_campus.jpg")
photo2=ImageTk.PhotoImage(img2)

ph2=Label(image=photo2)
ph2.place(x=400,y=378)

Scrollbar=Scrollbar(root)
Scrollbar.grid(row=10,column=3,columnspan=100)

#----------------------------------------------------------------Created Variables for Particular Events-------------------------------------------------#

student_name=StringVar()
scholar_number=StringVar()
stream=StringVar()
phone=StringVar()
father=StringVar()
mother=StringVar()
address=StringVar()

#----------------------------------------------------------------Created Labels-------------------------------------------------#

label0=Label(root,text="STUDENT MANAGEMENT SYSTEM",font="verdana  20 bold italic",relief=SUNKEN,bg="steel blue",fg="white",padx=15)
label0.place(x=400,y=7)

label1=Label(root,text="Student Name:")
label1.place(x=18,y=134)

label2=Label(root,text="Scholar Number:")
label2.place(x=18,y=164)

label3=Label(root,text="Stream:")
label3.place(x=18,y=194)

label4=Label(root,text="Phone Number:")
label4.place(x=18,y=224)

label5=Label(root,text="Father Name:")
label5.place(x=18,y=254)

label6=Label(root,text="Mother Name:")
label6.place(x=18,y=284)

label7=Label(root,text="Address:")
label7.place(x=18,y=314)

#----------------------------------------------------------------Entry Widget-------------------------------------------------#

e1=Entry(root,textvariable=student_name,relief=SUNKEN,bg='powder blue')
e1.place(x=140,y=136)

e2=Entry(root,textvariable=scholar_number,relief=SUNKEN,bg='powder blue')
e2.place(x=140,y=166)

e3=Entry(root,textvariable=stream,relief=SUNKEN,bg='powder blue')
e3.place(x=140,y=196)

e4=Entry(root,textvariable=phone,relief=SUNKEN,bg='powder blue')
e4.place(x=140,y=226)
    
e5=Entry(root,textvariable=father,relief=SUNKEN,bg='powder blue')
e5.place(x=140,y=256)

e6=Entry(root,textvariable=mother,relief=SUNKEN,bg='powder blue')
e6.place(x=140,y=286)

e7=Entry(root,textvariable=address,relief=SUNKEN,bg='powder blue')
e7.place(x=140,y=316)

#----------------------------------------------------------------Created Text Box Widget and Initialised The Scrollbar-------------------------------------------------#

t1=Text(root,width=110,height=20,yscrollcommand=Scrollbar.set)
t1.grid(row=11,column=1)

#----------------------------------------------------------------Configuration of Scrollbar-------------------------------------------------#

Scrollbar.config(command=t1.yview)   

#----------------------------------------------------------------Buttons-------------------------------------------------#

b1=Button(root,text="ADD STUDENT",command=add_student,width=40,bg='steel blue',fg='white',relief=SUNKEN)
b1.grid(row=12,column=0)

b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=40,bg='steel blue',fg='white',relief=SUNKEN)
b2.grid(row=13,column=0)

b3=Button(root,text="DELETE STUDENT",command=delete_student,width=40,bg='steel blue',fg='white',relief=SUNKEN)
b3.grid(row=14,column=0)

b4=Button(root,text="UPDATE INFO",command=update_student,width=40,bg='steel blue',fg='white',relief=SUNKEN)
b4.grid(row=15,column=0)

b5=Button(root,text="CLEAR",command=clear,width=40,bg='steel blue',fg='white',relief=SUNKEN)
b5.grid(row=16,column=0)

b6=Button(root,text="CLOSE",command=close,width=40,bg='steel blue',fg='white',relief=SUNKEN)
b6.grid(row=17,column=0)

#----------------------------------------------------------------Main Window-------------------------------------------------#

root.mainloop()
