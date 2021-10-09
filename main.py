from tkinter import*
from tkinter import messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1366x700+0+0")
        self.root.resizable(False,False)
        self.homepage()
    def homepage(self):
        frameback1=Frame(self.root,bg="grey")
        frameback1.place(x=0,y=0,height=700,width=1366)
        framefront1=Frame(self.root,bg='white')
        framefront1.place(x=320,y=130,height=450,width=500)
        but_in=Button(self.root,command =self.loginpage,bg="orange",fg="white",text="Sign In ",cursor="hand2",width="15",font=("times new roman",20))
        but_in.place(x=455,y=260)
        but_up=Button(self.root,command=self.registerpage,bg="orange",fg="white",text="Sign Up ",cursor="hand2",width="15",font=("times new roman",20))
        but_up.place(x=455,y=390)
    def loginpage(self):
        frameback2=Frame(self.root,bg="grey")
        frameback2.place(x=0,y=0,height=700,width=1366)
        framefront2=Frame(self.root,bg='white')
        framefront2.place(x=420,y=130,height=450,width=300)
        label1=Label(root,text="Login",font=('impact',32,'bold'),bg="white",fg="black" )
        label1.place(x=520,y=140)
        label2=Label(root,text="Username",font=("Goudy old style",20,"bold"), bg="white",fg="orange")
        label2.place(x=470,y=250)
        self.entry_username=Entry(root,font=("times new roman",15,"bold"),bg="white")
        self.entry_username.place(x=470,y=300)
        label3=Label(root,text="Password",font=("Goudy old style",20,"bold"), bg="white",fg="orange")
        label3.place(x=470,y=350)
        self.entry_password=Entry(root,font=("times new roman",15,"bold"),bg="white")
        self.entry_password.place(x=470,y=400)
        but1=Button(root,command=self.login,cursor="hand2",text="Login", font=("times new roman",15),fg="white",bg="orange",bd=0,width=15,height=1)
        but1.place(x=480,y=470)
        but2=Button(root,command=self.registerpage,text="Not Registered? Sign up here",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
        but2.place(x=490,y=520)
    def login(self):
        if self.entry_username.get()=="" or self.entry_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',database='test1')
                cur=con.cursor()
                cur.execute('select * from users where User_Name=%s and Password=%s',(self.entry_username.get(),self.entry_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
                    self.loginclear()
                    self.entry_username.focus()
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                 messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)
    def registerpage(self):
        frameback3=Frame(self.root,bg="grey")
        frameback3.place(x=0,y=0,height=700,width=1366)
        framefront3=Frame(self.root,bg='white')
        framefront3.place(x=420,y=130,height=500,width=300)
        label5=Label(root,text="Register",font=('impact',32,'bold'),bg="white",fg="black" )
        label5.place(x=490,y=140)
        label6=Label(root,text="Username",font=("Goudy old style",20,"bold"), bg="white",fg="orange")
        label6.place(x=470,y=230)
        self.choose_username=Entry(root,font=("times new roman",15,"bold"),bg="white")
        self.choose_username.place(x=470,y=280)
        label7=Label(root,text="Password",font=("Goudy old style",20,"bold"), bg="white",fg="orange")
        label7.place(x=470,y=330)
        self.choose_password=Entry(root,font=("times new roman",15,"bold"),bg="white")
        self.choose_password.place(x=470,y=380)
        label8=Label(root,text="Confirm Password",font=("Goudy old style",20,"bold"), bg="white",fg="orange")
        label8.place(x=470,y=430)
        self.confirm_password=Entry(root,font=("times new roman",15,"bold"),bg="white")
        self.confirm_password.place(x=470,y=480)
        but3=Button(root,command=self.register,cursor="hand2",text="Register", font=("times new roman",15),fg="white",bg="orange",bd=0,width=15,height=1)
        but3.place(x=480,y=540)
        but4=Button(root,command=self.loginpage,text="Already Registered? Sign in here",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
        but4.place(x=490,y=590)
    def register(self):
        if self.choose_username.get()==""or self.choose_password.get()==""or self.confirm_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.choose_password.get()!=self.confirm_password.get():
            messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",database="test1")
                cur=con.cursor()
                cur.execute("select * from users where User_Name=%s",self.choose_username.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another Username",parent=self.root)
                    self.regclear()
                    self.choose_username.focus()
                else:
                    cur.execute("insert into users values(%s,%s)",(self.choose_username.get(),self.choose_password.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Succesfull",parent=self.root)
                    self.loginpage()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)
    def appscreen(self):
        mainpage=Frame(self.root,bg="white")
        mainpage.place(x=0,y=0,height=700,width=1366)
        label4=Label(root,text="Homepage",font=('times new roman',32,'bold'),fg="black",bg='white')
        label4.place(x=375,y=100)
    def loginclear(self):
        self.entry_username.delete(0,END)
        self.entry_password.delete(0,END)
    def regclear(self):
        self.choose_username.delete(0,END)
        self.choose_password.delete(0,END)
        self.confirm_password.delete(0,END)
root=Tk()
ob=Login(root)
root.mainloop()
