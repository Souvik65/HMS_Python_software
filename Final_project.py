import tkinter.messagebox
from tkinter import  *
import mysql.connector as sqlcon #pip install mysql-connector-python
import random as rd
from PIL import ImageTk,Image    #pip install pillow
import customtkinter as ctk      #pip install customtkinter
from random import choice
from tkcalendar import DateEntry  #pip install tkcalendar
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

#----------------------------------------------Loading....----------------------------------------------------------------------------

i=0
def loading():
    root10 = Tk()
    image = PhotoImage(file='vector2.png')
    height = 600
    width = 600
    x = (root10.winfo_screenwidth()//2)-(width//2)
    y = (root10.winfo_screenheight()//2)-(height//2)
    root10.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root10.overrideredirect(True)
    root10.config(background='blue')
    window_label=Label(text="LIFE & CARE HOSPITAL",bg='blue',font=('Stencil',30,'bold'),fg="#FFFFFF")
    window_label.place(x=90,y=50)
    bg_label=Label(root10,image=image,bg='blue')
    bg_label.place(x=150,y=150)
    progress_label=Label(root10,text="Loading.......",font=('Trebuchet Ms',30,'bold'),fg="#FFFFFF",bg='blue')
    progress_label.place(x=160,y=450)
    progress=ttk.Style()
    progress.theme_use('clam')
    progress.configure("red.Horizontal.TProgressbar",background='#108cff')
    progress=Progressbar(root10,orient=HORIZONTAL, length=500,mode='determinate',style="red.Horizontal.TProgressbar" )
    progress.place(x=50,y=530)
    def load():
        global i
        if i<=10:
            text='Loading.....'+(str(10*i)+'%')
            progress_label.config(text=text)
            progress_label.after(600, load)
            progress['value']=10*i
            i+=1
        else:
            root10.withdraw()
            root10.destroy()
    load()
    root10.resizable(False, False)
    root10.mainloop()

loading()
#------------------------------------------------------------------------------------------------------------------------------------------

con=sqlcon.connect(host="localhost",user="root",password="kivuos10390")  #connection to mysql 
cur=con.cursor()

if (con):
    # mysql connection check
    print ("Connection successful")
else:
    print ("Connection unsuccessful")
    
cur.execute("create database if not exists Hospital")
cur.execute("use Hospital")
cur.execute('''create table if not exists appointment
            (
            phone varchar(10) primary key,
            name char(50),
            age char(3),
            gender char(6),
            bg varchar(3));''')

cur.execute("create table if not exists appointment_details"
            "("
            "phone varchar(12) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")

cur.execute("create table if not exists medicine_list"
            "("
            "phone varchar(10) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")


#  Message for registration
def entry():
    global e1,e2,e3,e4,e5
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    try:
        cur=con.cursor()
        query='insert into appointment values("{}", "{}", "{}", "{}", "{}")'.format(p1,p2,p3,p4,p5)
        cur.execute(query)
        con.commit()
        print ("insert successful")
        tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")
    except:
        tkinter.messagebox.showwarning("ERROR", "\n THIS NUMBER IS ALREADY REGISTERED",)
        print ("insert unsuccessful")
        con.rollback()
#  For registration 
def register():
    global e1,e2,e3,e4,e5,img
    root1=Toplevel()
    root1.title("Registration")
    root1.geometry("750x750+500+150")
    img=PhotoImage(file='login.png')
    img_label=Label(root1,image=img)
    img_label.place(x=0,y=0,relwidth=1,relheight=1)
    label=Label(root1,text="REGISTER YOURSELF",fg='blue',bg='#F0F0F0',font=('Sitka Small Semibold', 35, 'bold'))
    label.place(x=60,y=5)
    l1=Label(root1,text="Mobile NO.",font=('Sitka Small Semibold', 20, 'bold'))
    l1.place(x=80,y=130)        
    e1=tkinter.Entry(root1,width=20,font=('Sitka Small Semibold', 20))
    e1.place(x=320,y=130)
    l2=Label(root1,text="Full Name",font=('Sitka Small Semibold', 20, 'bold'))
    l2.place(x=80,y=200)
    e2=tkinter.Entry(root1,width=20,font=('Sitka Small Semibold', 20))
    e2.place(x=320,y=200)
    l3=Label(root1,text="AGE",font=('Sitka Small Semibold', 20, 'bold'))
    l3.place(x=80,y=290)
    e3=tkinter.Entry(root1,width=20,font=('Sitka Small Semibold', 20))
    e3.place(x=320,y=290)
    l4=Label(root1,text="Gemder     \nMale\Female",font=('Sitka Small Semibold', 18, 'bold'))
    l4.place(x=80,y=340)
    e4=tkinter.Entry(root1,width=20,font=('Sitka Small Semibold', 20))
    e4.place(x=320,y=360)
    l5=Label(root1,text="BLOOD GROUP",font=('Sitka Small Semibold', 20, 'bold'))
    l5.place(x=80,y=440)
    e5=tkinter.Entry(root1,width=20,font=('Sitka Small Semibold', 20))
    e5.place(x=320,y=440)
    b1=Button(root1,width=39,pady=2,text="REGISTER",font=('Sitka Small Semibold', 15),bg='blue',fg='white', command=lambda:[entry(),apoint()])
    b1.place(x=110,y=590)
    s6 = ctk.CTkButton(root1, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root1.destroy)
    s6.place(x=10,y=550)    
    root1.resizable(False,False)
    root1.mainloop()
    
#  For mobile no input
def apoint():
    global x1
    root2=Toplevel()
    root2.title("Appointment")
    root2.geometry("750x750+500+150")
    label=Label(root2,text="APPOINTMENT",font=(" Comic Sans MS" ,35, "bold"),fg='blue')
    label.pack()
    l1=Label(root2,text="Mobile NO.",font=(" Comic Sans MS" ,35, "bold"),fg='blue')
    l1.place(x=10,y=130)
    x1=tkinter.Entry(root2,font=(" Comic Sans MS" ,25, "bold"),fg='blue')
    x1.place(x=290,y=130)
    b1=ctk.CTkButton(root2, text="Submit",font=(" Comic Sans MS" ,30, "bold"),command=lambda:[get_apoint()])
    b1.place(x=100,y=190)
    s9 = ctk.CTkButton(root2, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root2.destroy)
    s9.place(x=10,y=550)
    root2.resizable(False,False)
    root2.mainloop()

#  For appointment
def get_apoint():
    global x1,x2,x3,x4
    p1=x1.get()  
    cur.execute('select * from appointment where phone=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        #tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!! \n PLEASE REGISTER FIRST",)
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!! \n PLEASE REGISTER FIRST\n for registration press ok")
        return register()
    else:
        root3=Tk()
        root3.geometry("750x750+500+150")
        label=Label(root3,text="APPOINTMENT",font='arial 25 bold')
        label.pack()
        if i[3]=='Male' or i[3]=='male':
                x="Mr."
                name2=Label(root3,text=i[1])
                name2.place(x=190,y=80)
        else:
                x="Mrs\Ms."
                name2=Label(root3,text=i[1])
                name2.place(x=190,y=80)
        for i in dat:
            name=Label(root3,text='WELCOME')
            name.place(x=50,y=80)
            name1=Label(root3,text=x)
            name1.place(x=150,y=80)
            age=Label(root3,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root3,text=i[2])
            age1.place(x=190,y=100)
            phone=Label(root3,text='GENDER:-')
            phone.place(x=50,y=120)
            phone1=Label(root3,text=i[3])
            phone1.place(x=190,y=120)
            bg=Label(root3,text='BLOOD GROUP:-')
            bg.place(x=50,y=140)
            bg1=Label(root3,text=i[4])
            bg1.place(x=190,y=140)
        L=Label(root3,text='DEPARTMENTS')
        L.place(x=50,y=220)
        L1=Label(root3,text="1.X-Ray ")
        L1.place(x=50,y=250)
        L2=Label(root3,text='2.Blood Test')
        L2.place(x=50,y=270)
        L3=Label(root3,text='3.Diabetes test')
        L3.place(x=50,y=290)
        L4=Label(root3,text='4.Ultrasound')
        L4.place(x=50,y=310)
        L5=Label(root3,text='5.Stool Test')
        L5.place(x=50,y=330)
        L6=Label(root3,text='6.Thyroid test')
        L6.place(x=50,y=350)
        L7=Label(root3,text='Enter your choice')
        L7.place(x=100,y=370)
        x2=tkinter.Entry(root3)
        x2.place(x=290,y=370)
        L7=Label(root3,text=('enter date')).place(x=100,y=400)
        x3=DateEntry(root3)
        x3.place(x=290,y=400)
        L8=Label(root3,text=('enter time in 24 hour format')).place(x=48,y=430)
        x4=tkinter.Entry(root3)
        x4.place(x=290,y=430)
        B1=Button(root3,text='Submit',command=lambda:[apo_details(),root3.destroy()])
        B1.place(x=120,y=480)
        s6 = ctk.CTkButton(root3, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root3.destroy)
        s6.place(x=10,y=550)
        root3.resizable(False,False)
        root3.mainloop()

#  Message for appointment
def apo_details():
    global x1,x2,h,p1,p2,p3,o,x4,x3
    a1=x2.get()
    a2=x3.get_date()
    a3=x4.get()
    if int(a1)==1:
        i=("Dr. a \nRoom no:- 10")
        j=("Dr. b \nRoom no:- 11")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)
        det=("Your appointment is fixed with\n",h,
             "\nDate:-",a2,
             "\nTime:-",a3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(a1,h,a2,a3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
    elif int(a1)==2:
        i=("Dr. j \nRoom no. 16")
        j=("Dr. i \nRoom no. 17")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with\n",h,
             "\nDate:-",a2,
             "\nTime:-",a3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(a1,h,a2,a3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
    elif int(a1)==3:
        i=("Dr. p \nRoom no. 12")
        j=("Dr. y \nRoom no. 13")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with\n",h,
             "\nDate:-",a2,
             "\nTime:-",a3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(a1,h,a2,a3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

    elif int(a1)==4:
        i=("Dr. k, \nRoom no. 18")
        j=("Dr. e \nRoom no. 19")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with\n",h,
             "\nDate:-",a2,
             "\nTime:-",a3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(a1,h,a2,a3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
    elif int(a1)==5:
        i=("Dr. i \nRoom no. 14")
        j=("Dr. d \nRoom no. 15")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with\n",h,
             "\nDate:-",a2,
             "\nTime:-",a3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(a1,h,a2,a3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
    elif int(a1)==6:
        i=("Dr. h \nRoom no. 001")
        j=("Dr. v \nRoom no. 002")
        k=("Dr. a \nRoom no. 003")
        l=("Dr. p \nRoom no. 004")
        q=(i,j,k,l)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with\n",h,
             "\nDate:-",a2,
             "\nTime:-",a3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(a1,h,a2,a3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
    else:
        tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER CORRECT INFORMATION')

#  List of doctors
def doc_lst():
    root4=Toplevel()
    root4.title("Doctor List")
    root4.geometry("750x750+500+150")
    
    l=["Dr.Amit Vatkar"," Dr.Lekha Mishra","Dr.Sandeep singh","Dr. Prithvi das","Dr. Ajay Bhatt","Dr. Vinod Trehan","Dr.Z.S. Raina","Dr. Aroop Rajgopal","Dr Udgeath Luthra","Dr Hemant Oberoi",'Dr. Rakesh Vaishya','Dr. Harnarayan Vaid',
       'Dr.M k barman','Dr. Kunal']
    
    m=["Internal medicine","Orthopedics","Neurosurgeon","Orthopaedic and \nJoint Replacement Surgeon","Cardiac Surgeon","Medical Oncologist","Cardiac Surgeon","MBBS","Cardiothoracic","Trauma & Orthopedic","Orthopedics","Dermatologist","Gynecologist","Pathologist"]
    
    n=['B11','C20','A10','A24','B5','C26','D7','D8','B10','C10','D11','A12','B13','D14']
    buttons=['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13','B14']

    l1=Label(root4,text='NAME OF DOCTORS',font=(" Comic Sans MS" ,13, "bold")) 
    l1.place(x=10,y=10)
    count=10
    for i in l:
       count=count+45
       l=Label(root4,text=i,font=(" Comic Sans MS" ,13, "bold"))
       l.place(x=20,y=count)

    l2=Label(root4,text='DEPARTMENT',font=(" Comic Sans MS" ,13, "bold"))
    l2.place(x=210,y=10)
    count1=10
    for i in m:
       count1=count1+45
       l3=Label(root4,text=i,font=(" Comic Sans MS" ,13, "bold"))
       l3.place(x=220,y=count1)

    l4=Label(root4,text='ROOM NO',font=(" Comic Sans MS" ,13, "bold"))
    l4.place(x=370,y=10)
    count2=10
    for i in n:
       count2=count2+45
       l5=Label(root4,text=i,font=(" Comic Sans MS" ,13, "bold"))
       l5.place(x=400,y=count2)


    #for appoint buttons
  
    l5=Label(root4,text='Appoinment',font=(" Comic Sans MS" ,15, "bold"))
    l5.place(x=530,y=10)
    count3=5
    for i in buttons:
        count3=count3+36
        
        l6=ctk.CTkButton(root4, text = 'Appoint',font=(" Comic Sans MS" ,10, "bold"),width=10, command=lambda:[apoint()])
        l6.place(x=450,y=count3)
    s1 = ctk.CTkButton(root4, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root4.destroy)
    s1.place(x=10,y=550) 
    root.resizable(False,False)
    root4.mainloop()

#Available Services
def ser_avail():
    global x5,add
    root5=Toplevel()
    root5.title("Services Available")
    root5.geometry("750x750+500+150")
    l1=Label(root5,text='Available Services',font=(" Comic Sans MS" ,20, "bold"))
    l1.place(x=20,y=10)
    f=["X-Ray","ECG","MRI","Blood Testing","Diabetes testing","Thyroid testing","Ultrasonography","Urinalysis","Stool Test"]
    count1=20
    for i in f:
       count1=count1+40
       l3=Label(root5,text=i,font=(" Comic Sans MS" ,15, "bold"))
       l3.place(x=60,y=count1)
    l2=Label(root5,text='ROOM NO.',font=(" Comic Sans MS" ,20, "bold"))
    l2.place(x=350,y=10)
    g=['A5','A2','D9','B9','B13','C6','A7','D10','D15']
    count2=30
    for i in g:
       count2=count2+40
       l4=Label(root5,text=i,font=(" Comic Sans MS" ,15, "bold"))
       l4.place(x=390,y=count2)
    l5=Label(root5,text='For booking service Call/Whatsapp.:- 7042856955 or 1800-600-500',font=(" Comic Sans MS" ,15, "bold"))
    l5.place(x=20,y=440)
    h1=Label(root5,text="Medical stuff(eg-Medicine,Blood,etc)",font=(" Comic Sans MS" ,25, "bold"),fg='blue')
    h1.place(x=20,y=510)
    x5=tkinter.Entry(root5,font=(" Comic Sans MS" ,25, "bold"),fg='blue',width=30)
    x5.place(x=30,y=560)
    add=x5.get()
    b1 = ctk.CTkButton(root5, text="Search",font=(" Comic Sans MS" ,20, "bold"),command=lambda:[view_med()])
    b1.place(x=100,y=500)

    s2 = ctk.CTkButton(root5, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root5.destroy)
    s2.place(x=10,y=550)
    root5.resizable(False,False) 
    root5.mainloop()


def view_med():
    global q1
    q1=x5.get()
    cur.execute('select * from medicine_list where medicine=(%s)',(q1,))
    datt=cur.fetchall()
    print(datt)
    a=[]
    for i in datt:
        a.append(i)
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        dett=a
        tkinter.messagebox.showinfo("Medical stuff",dett)


#####------------profile view--------

def search_data():
    global x3,ad
    root7=Toplevel()
    root7.title("Profile View")
    root7.geometry("750x750+500+150")
    img=PhotoImage(file='5.png')
    Label(root7,image=img,bg='white',height=400,width=750).place(x=10,y=300)
    label=Label(root7,text="SEARCH DATA",font=(" Comic Sans MS" ,40, "bold"),fg='blue')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    l1=Label(root7,text="Mobile NO.",font=(" Comic Sans MS" ,25, "bold"),fg='blue')
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root7,font=(" Comic Sans MS" ,25, "bold"),fg='blue')
    x3.place(x=200,y=130)
    ad=x3.get()
    b1 = ctk.CTkButton(root7, text="Search",font=(" Comic Sans MS" ,30, "bold"),command=lambda:[view_data()])
    b1.place(x=150,y=160)
    s4 = ctk.CTkButton(root7, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root7.destroy)
    s4.place(x=10,y=550)
    root7.resizable(False,False)
    root7.mainloop()

def view_data():
    global p1
    p1=x3.get()
    cur.execute('select * from appointment where phone=(%s)',(p1,))
    dat=cur.fetchall()
    print(dat)
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        det=a
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)


#########----------UPDATE-----------

def do_modify():
    global ad,x3,x4,x5
    ad=x3.get()
    choice=x4.get()
    new=x5.get()
    if choice=='1':
        print("matha")
        ass=cur.execute('update appointment set name=(%s) where phone=(%s)',(new,ad))
        if (ass):
            print("done")
        else:
            print("no")
    elif choice=='2':
        cur.execute('update appointment set age=(%s) where phone=(%s)',(new,ad))        
    elif choice=='3':
        cur.execute('update appointment set gender=(%s) where phone=(%s)',(new,ad))
    elif choice=='4':
        cur.execute('update appointment set phone=(%s) where phone=(%s)',(new,ad))    
    elif choice=='5':
        cur.execute('update appointment set bg=(%s) where phone=(%s)',(new,ad))
    else:
        pass
    tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED")

def modify():
    global x3,x4,choice,new,x5,root6
    p1=x3.get()
    cur.execute('select * from appointment where phone=(%s)',(p1,))
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root6=Tk()
        root6.geometry("750x750+500+150")
        l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
        l1.place(x=75,y=10)
        l2=Label(root6,text='WHAT YOU WANT TO CHANGE')
        l2.place(x=50,y=200)
        l3=Label(root6,text='1.NAME')
        l3.place(x=50,y=220)
        l4=Label(root6,text='2.AGE')
        l4.place(x=50,y=240)
        l5=Label(root6,text='3.GENDER')
        l5.place(x=50,y=260)
        l6=Label(root6,text='4.BLOOD GROUP')
        l6.place(x=50,y=280)
        x2=Label(root6,text='Enter :-')
        x2.place(x=50,y=330)
        x4=tkinter.Entry(root6)
        choice=x4.get()
        x4.place(x=100,y=330)
        for i in dat:
                name=Label(root6,text='NAME:-')
                name.place(x=50,y=80)
                name1=Label(root6,text=i[1])
                name1.place(x=190,y=80)
                age=Label(root6,text='AGE:-')
                age.place(x=50,y=100)
                age1=Label(root6,text=i[2])
                age1.place(x=190,y=100)
                gen=Label(root6,text='GENDER:-')
                gen.place(x=50,y=120)
                gen1=Label(root6,text=i[3])
                gen1.place(x=190,y=120)
                pho=Label(root6,text='BLOOD GROUP:-')
                pho.place(x=50,y=140)
                pho1=Label(root6,text=i[4])
                pho1.place(x=190,y=140)
                b=Button(root6,text='Submit',command=do_modify)
                b.place(x=50,y=400)
                L1=Label(root6,text='OLD DETAILS :-')
                L1.place(x=50,y=50)
                L2=Label(root6,text='ENTER NEW DETAIL :-')
                L2.place(x=50,y=360)
                x5=tkinter.Entry(root6)
                new=x5.get()
                x5.place(x=200,y=360)
                root6.mainloop()


choice=None
new=None    
ad=None
def mod_sub():
    global x3,ad
    root8=Tk()
    root8.geometry("750x750+500+150")
    label=Label(root8,text="MODIFICATION",font=(" Comic Sans MS" ,40, "bold"),fg='blue')
    label.pack()
    frame=Frame(root8,height=200,width=200)
    frame.pack()
    l1=Label(root8,text="Mobile NO.",font=(" Comic Sans MS" ,25, "bold"),fg='blue')
    l1.place(x=10,y=130)
    x3=tkinter.Entry(root8,font=(" Comic Sans MS" ,25, "bold"),fg='blue')
    x3.place(x=210,y=130)
    ad=x3.get()
    b1 = ctk.CTkButton(root8, text="Submit",font=(" Comic Sans MS" ,30, "bold"),command=lambda:[modify()])
    b1.place(x=100,y=160)
    s5 = ctk.CTkButton(root8, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=root8.destroy)
    s5.place(x=10,y=550)
    root8.resizable(False,False)
    root8.mainloop()

###-----------------------------------------------

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_entry.get("1.0", END)
    # Save the feedback data to a file
    with open("feedback.txt", "a") as file:
        file.write("Name: " + name + "\n")
        file.write("Email: " + email + "\n")
        file.write("Feedback: " + feedback + "\n")
        file.write("-" * 20 + "\n")
    # Clear the form entries
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    feedback_entry.delete("1.0", END)
    tkinter.messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
    
def submit_box():
    global name_entry,email_entry,feedback_entry
    root9 = Toplevel()
    root9.geometry("750x750+500+150")
    root9.title("Feedback Form")
    name_label = Label(root9, text="Name:")
    name_label.pack()
    name_entry = Entry(root9,font=("Comic Sans MS", 10))
    name_entry.pack()
  
    email_label = Label(root9, text="Email:")
    email_label.pack()
    email_entry = Entry(root9,font=("Comic Sans MS", 10))
    email_entry.pack()
    
    feedback_label = Label(root9, text="Feedback:")
    feedback_label.pack()
    feedback_entry = Text(root9, height=10)
    feedback_entry.pack()
    
    submit_button = Button(root9, text="Submit", command=lambda:[submit_feedback()])
    submit_button.pack()
    img=PhotoImage(file='1234.png')
    Label(root9,image=img,bg='white',height=400,width=750).place(x=10,y=300)
    s3 = ctk.CTkButton(root9, text="Back",font=('Comic Sans MS ',10 ,'bold'),width=10,command=lambda:[root9.destroy()])
    s3.place(x=10,y=550)
    root9.mainloop()


class SlidePanel(ctk.CTkFrame):
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent,fg_color='#EBEBEB')

		# general attributes 
		self.start_pos = start_pos + 0.04
		self.end_pos = end_pos - 0.03
		self.width = abs(start_pos - end_pos)

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.9)

	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
		else:
			self.animate_backwards()

	def animate_forward(self):
		if self.pos > self.end_pos:
			self.pos -= 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos < self.start_pos:
			self.pos += 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True

def move_btn():
	global button_x
	button_x += 0.001
	button.place(relx = button_x, rely = 0.5, anchor = 'center')
	
	if button_x < 0.9:
		root.after(10, move_btn)

# window 
root = ctk.CTk()
root.title("Life and Care HOSPITAL")
ctk.set_appearance_mode('light')



# animated widget
animated_panel = SlidePanel(root, 1.0, 0.8)
ctk.CTkButton(animated_panel, text = "View Profile",command=search_data, corner_radius = 20).pack( fill = 'both', pady = 9)
ctk.CTkButton(animated_panel, text = "Update Profile",command=mod_sub, corner_radius = 20).pack( fill = 'both', pady = 9)
ctk.CTkButton(animated_panel, text = 'Feedback',command=submit_box, corner_radius = 20).pack( fill = 'both', pady = 9)

button_x = 0.9
button = ctk.CTkButton(root, text = 'Menu',font=(" Sitka Small Semibold" ,15, "bold"),width=10, command = animated_panel.animate)
button.place(x=1,y=1)
root.geometry("600x600+500+150")
label=Label(root,text="L & C HOSPITAL",font=("Sitka Small Semibold", 40, "bold"),bg='#EBEBEB',fg='Blue')

b1 = ctk.CTkButton(root, text="Registration",font=(" Sitka Small Semibold" ,30, "bold"),command=lambda:[register()])
b2 = ctk.CTkButton(root, text="Available Services",font=('Sitka Small Semibold', 30, 'bold'),command=ser_avail)
b3 = ctk.CTkButton(root, text="Doctors List",font=("Sitka Small Semibold" ,30 ,"bold"),command=doc_lst)
b6 = ctk.CTkButton(root, text="Exit",font=('Sitka Small Semibold ',30 ,'bold'),command=root.destroy)
label.place(x=100,y=10)
b1.place(x=200,y=150)
b3.place(x=200,y=250)
b2.place(x=170,y=350)
b6.place(x=240,y=450)

root.resizable(False,False)
root.mainloop()








    
