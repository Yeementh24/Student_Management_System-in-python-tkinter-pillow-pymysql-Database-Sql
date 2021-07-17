from tkinter import *
from tkinter import ttk,messagebox
from tkinter.font import BOLD
from PIL import Image,ImageTk#pip install pillow
import pymysql
from pymysql.cursors import Cursor#pip install pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')

        #===BackGround Image===#
        self.bg=ImageTk.PhotoImage(file="images/firstbg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #===Left Image===#
        self.left=ImageTk.PhotoImage(file="images/SecondLeft.png")
        left=Label(self.root,image=self.left).place(x=80,y=100)#,width=400,height=500)

        #===Register Frame===#
        frame1=Frame(self.root,bg='white')
        frame1.place(x=468,y=100,width=700,height=500)

        title=Label(frame1,text='Register Here',font=('time new roman',20,'bold'),bg='white',fg='green').place(x=250,y=30)

        #-----------------------Row1
        f_name=Label(frame1,text='First Name',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text='Last Name',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=350,y=100)
        self.txt_lname=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_lname.place(x=350,y=130,width=250)

        #-----------------------Row2
        contact_no=Label(frame1,text='Contact No.',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=50,y=160)
        self.txt_ContactNo=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_ContactNo.place(x=50,y=190,width=250)

        email_id=Label(frame1,text='Email Id',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=350,y=160)
        self.txt_emaileid=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_emaileid.place(x=350,y=190,width=250)

        #------------------------Row3
        question=Label(frame1,text='Security Question',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=50,y=220)
        self.cmb_question=ttk.Combobox(frame1,font=('time new roman',13),state='readonly',justify=CENTER)
        self.cmb_question['values']=('Select','Your First Pet Name','Your Birth Place','Your Best Friend Name')
        self.cmb_question.place(x=50,y=250,width=250)
        self.cmb_question.current(0)

        answer=Label(frame1,text='Answer',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=350,y=220)
        self.txt_answer=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_answer.place(x=350,y=250,width=250)

        #-----------------------Row4
        password=Label(frame1,text='Password',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=50,y=280)
        self.txt_password=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_password.place(x=50,y=310,width=250)

        confirm=Label(frame1,text='Confirm Password',font=('time new roman',10,'bold'),bg='white',fg='gray').place(x=350,y=280)
        self.txt_confirm=Entry(frame1,font=('time new roman',10),bg='light gray')
        self.txt_confirm.place(x=350,y=310,width=250)

        #-----------Terms&Conditions------------Row4
        self.var_chk=IntVar()
        checkBox=Checkbutton(frame1,text='I Agree The Terms & Conditions',variable=self.var_chk,onvalue=1,offvalue=0,bg='white',font=('time new roman',10,'bold')). place(x=50,y=350)

        btn_register= Button(frame1,text='Register',font=('time new roman',20,'bold'),bg='green',width=20,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=400)
        btn_signin= Button(self.root,text='Sign In',command=self.Sign_in,font=('time new roman',10,'bold'),bg='white',width=16,cursor='hand2').place(x=327,y=464)
    

    def Sign_in(self):
        self.root.destroy()
        import Login


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_ContactNo.delete(0,END)
        self.txt_emaileid.delete(0,END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_confirm.delete(0,END)
    
    def register_data(self):
        if self.txt_fname.get()=='' or self.txt_ContactNo.get()==''or self.txt_emaileid.get()=='' or self.cmb_question.get()=='Select' or self.txt_answer.get()=='' or self.txt_password.get()=='' or self.txt_confirm.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root)
        elif self.txt_password.get()!=self.txt_confirm.get():
            messagebox.showerror('Error','Password And Confirm Paswword Are Not Same\n Try Again!',parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror('Error','Agree Our Terms & Conditions',parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='employee')
                cur=con.cursor()
                cur.execute('select * from employee where email=%s',self.txt_emaileid.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','User Already Exist,Please try with another Email Id',parent=self.root)
                else:
                    cur.execute('insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_ContactNo.get(),
                                    self.txt_emaileid.get(),
                                    self.cmb_question.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Successful','Register Successful \nSign in',parent=self.root)
                    self.clear()


            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root)

            #messagebox.showinfo('Successful','Register Successful \nSign in',parent=self.root)
            
            


    
root=Tk()
obj=Register(root)
root.mainloop()