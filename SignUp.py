from tkinter import * 
from tkinter import messagebox 
import pymysql

def clear():
    user.delete(0,"end")
    code.delete(0,"end")
    confirm_code.delete(0,"end")

def connect_database():
    if user.get()=="" or code.get()=="" or confirm_code.get()=="":
        messagebox.showerror("Invalid","All Fields Are Reqired")

    elif code.get()!=confirm_code.get():
        messagebox.showerror("Invalid","Password Mismatch")
    
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="root123")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Invalid","Database Connectivity Issue")
            return
        try:
            query="Create Database File_Sharing_App"
            mycursor.execute(query)
            query="Use File_Sharing_App"
            mycursor.execute(query)
            query="create table userdata(id int auto_increment primary key not null,username varchar(50),password varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("Use file_sharing_app")
        query="Select * from userdata where username=%s"
        mycursor.execute(query,(user.get()))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror("Invalid","Username Already Exits")
        else:
            query="insert into userdata(username,password) values (%s,%s)"
            mycursor.execute(query,(user.get(),code.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","SuccessFully Registered")
            clear()
            window.destroy()
            import Login
            

def login_page():
    window.destroy()
    import Login
    
window=Tk()
window.title ("SignUp")
window.geometry("925x500+300+100") 
window.configure(bg="#fff")
window.resizable (False, False)

img = PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\SignUp.png")
Label (window, image=img, border=0, bg="white").place(x=50,y=90)
frame=Frame(window,width=350,height=390,bg="#fff")
frame.place (x=480,y=50)

heading=Label (frame,text="Sign up",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=100,y=5)
#######-----------------------------------------------
def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    if user.get()=="":
        user.insert(0,"Username")

user=Entry(frame, width=25, fg="black",border=0,bg="white", font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=80)
user.insert (0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame (frame, width=295, height=2,bg= "black").place(x=25,y=107)
#######-----------------------------------------------
def on_enter(e):
    code.delete(0,"end") 
def on_leave(e):
    if code.get()=="":
        code.insert(0,"Password")

code=Entry (frame, width=25, fg="black",border=0,bg="white", font=("Microsoft Yahei UI Light", 11))
code.place(x=30, y=150)
code.insert (0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame (frame, width=295, height=2,bg= "black").place(x=25,y=177)
#######----------------------------------------------
def on_enter(e):
    confirm_code.delete(0,"end") 
def on_leave(e):
    if confirm_code.get()=="":
        confirm_code.insert(0,"Confirm Password")

confirm_code=Entry (frame, width=25, fg="black",border=0,bg="white", font=("Microsoft Yahei UI Light", 11))
confirm_code.place(x=30, y=220)
confirm_code.insert (0,"Confirm Password")
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>",on_leave)

Frame (frame, width=295, height=2,bg= "black").place(x=25,y=247)
#######-----------------------------------------------

Button(frame,width=39, pady=7,text="Sign up",bg="#57a1f8",fg="white",border=0,command=connect_database).place(x=35,y=280)

label=Label(frame, text="I have an account",fg="black" ,bg="white", font=("Microsoft YaHei UI Light",9))
label.place (x=90, y=340)
signin=Button (frame,width=6, text= "Sign in", border=0, bg="white",cursor="hand2",fg="#57a1f8",command=login_page) 
signin.place(x=200,y=341)

window.mainloop()