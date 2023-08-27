from tkinter import *
from tkinter import messagebox
import pymysql

def signup_page():
    root.destroy()
    import SignUp

def sign_in():
    if user.get()=="" or code.get()=="":
        messagebox.showerror("Invalid","All Fields Are Reqired")
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="root123")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Invalid","Connection not Established")
            return
        
        query="Use File_Sharing_App"
        mycursor.execute(query)
        query="Select * from userdata where username=%s and password=%s"
        mycursor.execute(query,(user.get(),code.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Invalid","Invalid username or password")
        else:
            messagebox.showinfo("Success","Successfully Logged In")
            root.destroy()
            import Main

root=Tk()
root.title("Login")
root.geometry("925x500+300+150")
root.configure(bg="#fff")
root.resizable(False, False)



'''def signin():
    username=user.get()
    password=code.get()
    if username=="" and password=="":
        screen=Toplevel(root)
        screen.title("")
        screen.geometry ("925x500+300+200")
        screen.config(bg="white")
        Label(screen, text="",bg="#fff",font=("calibri (Body)",50,"bold")).pack(expand=True)
        screen.mainloop()
    elif username!="" and password!= "":
        messagebox.showerror ("Invalid","invalid username and password")
    elif password!="":
        messagebox.showerror ("Invalid","invalid password")    
    elif username!="":
        messagebox.showerror ("Invalid","invalid username")'''


img = PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\login.png")
Label(root, image=img, bg= "white").place(x=50, y=50) 

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading= Label(frame, text="Sign in",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=100,y=5)
########------------------------------           
def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")  

user = Entry(frame,width=25, fg="black",border=0,bg="white", font=("Microsoft YaHei UI Light", 11))
user.place (x=30,y=80)
user.insert(0, "Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25, y=107)
########-------------------------------
def on_enter(e):
    code.delete(0,"end")
def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")  

code = Entry (frame, width=25, fg="black",border=0,bg="white", font=("Microsoft YaHei UI Light", 11))
code.place (x=30,y=150)
code.insert (0,'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########-------------------------------

Button(frame,width=39,pady=7,text="Sign in",bg="#57a1f8",fg="white",border=0,command=sign_in).place(x=35,y=204)
label=Label(frame, text="Don't have an account?", fg="black",bg="white",font=("Microsoft YaHei UI Light",9)) 
label.place (x=75, y=270)

sign_up=Button(frame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#57a1f8",command=signup_page)
sign_up.place(x=215,y=270)

root.mainloop()
