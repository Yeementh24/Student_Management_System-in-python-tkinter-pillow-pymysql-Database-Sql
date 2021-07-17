from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Mangement System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='#B0C4DE')

        title=Label(self.root,text='Student Management System',bd=10,relief=GROOVE,font=('time new romans',30,'bold'),bg='yellow',fg='red')
        title.pack(side=TOP,fill=X)

        #=================All Variable===============
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        
        #===============MANAGE FRAME==========================================
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Manage_frame.place(x=15,y=80,width=450,height=560)

        m_title=Label(Manage_frame,text='Manage Student',font=('time new romans',20,'bold'),bg='crimson',fg='white')
        m_title.grid(row=0,columnspan=2,pady=20)

        roll_no=Label(Manage_frame,text='Roll No.',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        roll_no.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        rollNo=Entry(Manage_frame,textvariable=self.Roll_no_var,font=('time new roman',10,'bold'),bg='white',bd=5,relief=GROOVE)
        rollNo.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        Name=Label(Manage_frame,text='Name',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        Name.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        name=Entry(Manage_frame,textvariable=self.name_var,font=('time new roman',10,'bold'),bg='white',bd=5,relief=GROOVE)
        name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        Email=Label(Manage_frame,text='Email Id.',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        Email.grid(row=3,column=0,pady=10,padx=20,sticky='w')
        Email_Id=Entry(Manage_frame,textvariable=self.email_var,font=('time new roman',10,'bold'),bg='white',bd=5,relief=GROOVE)
        Email_Id.grid(row=3,column=1,pady=10,padx=20,sticky='w')

        Gender=Label(Manage_frame,text='Gender',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        Gender.grid(row=4,column=0,pady=10,padx=20,sticky='w')
        cmd_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=('time new roman',10,'bold'),state='readonly',justify=CENTER)
        cmd_gender['values']=('Select','Male','Female','0ther')
        cmd_gender.grid(row=4,column=1,padx=20,pady=10,sticky='w')
        cmd_gender.current(0)
        

        Contact_No=Label(Manage_frame,text='Contact No.',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        Contact_No.grid(row=5,column=0,pady=10,padx=20,sticky='w')
        contact=Entry(Manage_frame,textvariable=self.contact_var,font=('time new roman',10,'bold'),bg='white',bd=5,relief=GROOVE)
        contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')

        Birthday=Label(Manage_frame,text='D.O.B',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        Birthday.grid(row=6,column=0,pady=10,padx=20,sticky='w')
        dob=Entry(Manage_frame,textvariable=self.dob_var,font=('time new roman',10,'bold'),bg='white',bd=5,relief=GROOVE)
        dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')

        address=Label(Manage_frame,text='Address',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        address.grid(row=7,column=0,pady=10,padx=20,sticky='w')
        self.txt_address=Text(Manage_frame,width=20,height=3)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')
        #====button of Manage Frame===========

        button_frame=Frame(Manage_frame,bd=0,relief=RIDGE,bg='crimson')
        button_frame.place(x=10,y=480,width=430)

        but_add=Button(button_frame,text='Add',width=10,command=self.AddStudent).grid(row=0,column=0,padx=10,pady=10)
        but_update=Button(button_frame,text='Update',width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        but_delete=Button(button_frame,text='Delete',width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        but_clear=Button(button_frame,text='Clear',width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        
        #===============DETAIL FRAME==========================================
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Detail_frame.place(x=480,y=80,width=770,height=560)

        search=Label(Detail_frame,text='Search_By',font=('time new romans',18,'bold'),bg='crimson',fg='white')
        search.grid(row=0,column=0,pady=10,padx=20,sticky='w')
        cmdsearch=ttk.Combobox(Detail_frame,font=('time new roman',10,'bold'),textvariable=self.search_by,state='readonly',justify=CENTER)
        cmdsearch['values']=('Roll_No','Name','Contact')
        cmdsearch.grid(row=0,column=1,padx=20,pady=10,sticky='w')
        cmdsearch.current(0)

        Search=Entry(Detail_frame,font=('time new roman',10,'bold'),textvariable=self.search_txt,bg='white',bd=5,relief=GROOVE)
        Search.grid(row=0,column=2,pady=10,padx=20,sticky='w')
        #=====Button of Detail Frame=====
        but_Search=Button(Detail_frame,text='Search',width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        but_Showall=Button(Detail_frame,text='Show All',width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        #======================Table Frame===========================

        Table_frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg='crimson')
        Table_frame.place(x=10,y=50,height=490,width=740)

        scroll_x=Scrollbar(Table_frame,orient='horizontal')
        scroll_y=Scrollbar(Table_frame,orient='vertical')
        self.Student_table=ttk.Treeview(Table_frame,columns=('roll','name','email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading('roll',text='Roll No.')
        self.Student_table.heading('name',text='Name')
        self.Student_table.heading('email',text='Email')
        self.Student_table.heading('gender',text='Gender')
        self.Student_table.heading('contact',text='Contact No.')
        self.Student_table.heading('dob',text='D.O.B')
        self.Student_table.heading('address',text='Address')
        self.Student_table['show']='headings'
        self.Student_table.column('roll',width=100)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('gender',width=100)
        self.Student_table.column('contact',width=100)
        self.Student_table.column('dob',width=100)
        self.Student_table.column('address',width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()

    def AddStudent(self):
        if self.Roll_no_var.get()=='' or self.name_var.get()=='' or self.email_var.get()=='' or self.gender_var=='' or self.contact_var=='' or self.dob_var=='' or self.txt_address=='':
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='studentdata')
            cur=con.cursor()
            cur.execute('INSERT INTO studentdata VALUES(%s,%s,%s,%s,%s,%s,%s)',(self.Roll_no_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Student Added Successfully",parent=self.root)

    def fetch_data(self):
        con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='studentdata')
        cur=con.cursor()
        cur.execute('select * from studentdata')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_no_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.contact_var.set('')
        self.dob_var.set('')
        self.txt_address.delete('1.0',END)

    def get_cursor(self,ev ):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='studentdata')
        cur=con.cursor()
        cur.execute('UPDATE studentdata SET name=%s,email=%s,gender=%s,contact_no=%s,dob=%s,address=%s WHERE roll_no=%s',(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.Roll_no_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Sucess","Data Updated Successfully")

    def delete_data(self):
        con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='studentdata')
        cur=con.cursor()
        cur.execute('delete from studentdata where roll_no=%s',self.Roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host='localhost',port=3307,user='root',password='',database='studentdata')
        cur=con.cursor()
        cur.execute("select * from studentdata where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
       #cur.execute("select * from studentdata where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()


    
        






root=Tk()
obj=  Student(root)
root.mainloop()  
