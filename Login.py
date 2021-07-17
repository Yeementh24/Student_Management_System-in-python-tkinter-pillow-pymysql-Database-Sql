from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
from tkinter import ttk
import time 
from math import *
import pymysql
from tkinter import messagebox
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login Page')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#021e2f')

        #========Background Frame============
        left_lbl=Label(self.root,bg='#08A3D2',bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg='#031F3C',bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        
        #========Frames============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        
        left_login_frame=Label(login_frame,bg='#031F3C',bd=0)
        left_login_frame.place(x=0,y=0,relheight=1,width=351)

        right_login_frame=Label(login_frame,bg='#08A3D2',bd=0)
        right_login_frame.place(x=351,y=0,relheight=1,relwidth=1)

        title=Label(login_frame,text='Login Here',font=('time new roman',25,'bold'),bg='#08A3D2',fg='#FAFAD2').place(x=480,y=110)

        email_Add=Label(login_frame,text='Email Address',font=('time new roman',14,'bold'),bg='#08A3D2',fg='lightgray').place(x=380,y=210)
        self.txt_emailAdd=Entry(login_frame,font=('time new roman',10),bg='lightgray')
        self.txt_emailAdd.place(x=380,y=235,width=250)
        

        password=Label(login_frame,text='Password',font=('time new roman',14,'bold'),bg='#08A3D2',fg='lightgray').place(x=380,y=275)
        self.txt_loginpassword=Entry(login_frame,font=('time new roman',10),bg='lightgray')
        self.txt_loginpassword.place(x=380,y=300,width=250)
        

        btn_Signin= Button(login_frame,text='LOGIN',command=self.login,font=('time new roman',15,'bold'),bg='#B0C4DE',fg='black',width=10,height=1,bd=0,cursor='hand2').place(x=380,y=340)
        btn_Register_new_account= Button(login_frame,text='Register New Account',command=self.register_window,font=('time new roman',10,'bold'),bg='#08A3D2',fg='red',width=18,height=1,bd=0,cursor='hand2').place(x=380,y=400)
        btn_Foget_Password= Button(login_frame,text='Forget Password',font=('time new roman',10,'bold'),command=self.forget_password_window,bg='#08A3D2',fg='#00FF00',width=18,height=1,bd=0,cursor='hand2').place(x=530,y=348)

        #========Clock============
        self.lbl=Label(self.root,bg='white',bd=0)
        self.lbl.place(x=270,y=180,height=300,width=300)
        self.working()

    def reset(self):
        self.cmb_question.current(0)
        self.txt_newpassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_loginpassword.delete(0,END)
        self.txt_emailAdd.delete(0,END)


    def forget_pass(self):
        if self.cmb_question.get()=='Select' or self.txt_answer=='' or self.txt_newpassword=='':
            messagebox.showerror('Error','All Field Are Required',parent=self.root2)

        else:
            try:
                con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='employee')
                cur=con.cursor()
                cur.execute('select * from employee where email=%s and question=%s and answer=%s',(self.txt_emailAdd.get(),self.cmb_question.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please Select the Correct Security Question \n Also Enter the Correct Answer',parent=self.root2)
                else:
                    cur.execute('update employee set password=%s where email=%s',(self.txt_newpassword.get(),self.txt_emailAdd.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Password Change Successfully ,Please Login With New Password',parent=self.root2)
                    self.reset()
                    self.root2.destroy()
                    
                    
                    

            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root)

        

    def forget_password_window(self):
        if self.txt_emailAdd.get()=='':
            messagebox.showerror('Error','Please enter the email address to reset your password',parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='employee')
                cur=con.cursor()
                cur.execute('select * from employee where email=%s',(self.txt_emailAdd.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please Enter the Invalid Email then click on Forget Password',parent=self.root)
                    
                else:
                    con.close() 
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+450+150")
                    self.root2.config(bg='white')
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t=Label(self.root2,text='Forget Password?',font=('times new roman',20,'bold'),bg='white',fg='Red').place(x=0,y=10,relwidth=1)

                    question=Label(self.root2,text='Security Question',font=('time new roman',15,'bold'),bg='white',fg='gray').place(x=50,y=80)
                    self.cmb_question=ttk.Combobox(self.root2,font=('time new roman',13),state='readonly',justify=CENTER)
                    self.cmb_question['values']=('Select','Your First Pet Name','Your Birth Place','Your Best Friend Name')
                    self.cmb_question.place(x=50,y=110,width=250)
                    self.cmb_question.current(0)

                    answer=Label(self.root2,text='Answer',font=('time new roman',15,'bold'),bg='white',fg='gray').place(x=50,y=160)
                    self.txt_answer=Entry(self.root2,font=('time new roman',13),bg='light gray')
                    self.txt_answer.place(x=50,y=190,width=250)

                    new_password=Label(self.root2,text='New Password',font=('time new roman',15,'bold'),bg='white',fg='gray').place(x=50,y=240)
                    self.txt_newpassword=Entry(self.root2,font=('time new roman',13),bg='light gray')
                    self.txt_newpassword.place(x=50,y=270,width=250)

                    btn_change_password=Button(self.root2,text="Reset Password",bg='#24a0ed',fg='white',command=self.forget_pass,font=('times new roman',15,'bold')).place(x=100,y=310)   
                
            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root)
 
            

    def register_window(self):
        self.root.destroy()
        import registery


    def login(self):
        if self.txt_emailAdd.get()=='' or self.txt_loginpassword=='':
            messagebox.showerror('Error','All Fields Are Required',parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='employee')
                cur=con.cursor()
                cur.execute('select * from employee where email=%s and password=%s',(self.txt_emailAdd.get(),self.txt_loginpassword.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username & Password',parent=self.root)
                    
                else:
                    messagebox.showinfo('Success','Welcome',parent=self.root)
                    self.root.destroy()
                    import Student
                con.close() 


            except Exception as es:
                messagebox.showerror('Error',f'Error due to:{str(es)}',parent=self.root)
        

    def clock_image(self,hr,min_,sec_):
        clock=Image.new('RGB',(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #====For Clock Image=====
        bg=Image.open('images\clock.jpg')
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        # Formula to rotate the Anticlock
        # angle_in_radian= angle_in_degree * math.pi / 180
        # line_lenght = 100
        # center_x = 250
        # center_x = 250
        # end_x = center_x + line_lenght * math.cos(angle_in_radian)
        # end_y = center_y + line_lenght * math.sin(angle_in_radian)
        
        #====For Hour Line Image=====
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='black',width=4)
        #====For Munite Line Image=====
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill='blue',width=3)
        #====For sec Line Image=====
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill='green',width=4) 
        draw.ellipse((195,195,210,210),fill='black')     
        clock.save("images\clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        
        self.img=ImageTk.PhotoImage(file='images\clock_new.png')
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)


root=Tk()
obj=Login_window(root)
root.mainloop()
        