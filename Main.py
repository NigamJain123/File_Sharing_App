from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import socket
import os


def select_file():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("File_Type","*.txt"),("All Files","*.*")))
   
def sender():
    s=socket.socket()
    host=socket.gethostname()
    port=6000
    s.bind((host,port))
    s.listen(5)
    print(host)
    #messagebox.showinfo("Success","waiting for incoming connections.....")
    print("waiting for incoming connections.....")
    conn,addr=s.accept()
    file=open(filename,"rb")
    file_data=file.read(4096)
    conn.send(file_data)
    messagebox.showinfo("Success","Data has been Transmitted Successfully")
    #print("Data has been Transmitted Successfully")


def Send():
    #root.destroy()
    window=Toplevel()
    window.title("Send")
    window.geometry("450x560+570+100")
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    ##### icon #######
    image_icon1=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\WeTransfer.png")
    window.iconphoto(False,image_icon1)
    
    Sbackground=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\sender.png")
    Label(window,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\id.png")
    Label(window,image=Mbackground,bg="#f4fdfe").place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f"ID:{host}",bg="white",fg="black").place(x=200,y=295)

    Button(window,text="+ select file",width=10,height=1,font="arial 14 bold",bg="#fff",fg="#000",border=0,command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font="arial 14 bold",bg="#000",fg="#fff",border=0,command=sender).place(x=300,y=150)


    window.mainloop()

    
def Receive():
    main=Toplevel()
    main.title("Receive")
    main.geometry("450x560+570+100")
    main.configure(bg="#f4fdfe")
    main.resizable(False,False)

    def receiver():
        ID=SenderID.get()
        filename1=incoming_file.get()

        s=socket.socket()
        port=6000
        s.connect((ID,port)) 
        file=open(filename1,"wb")
        file_data=s.recv(4096)
        file.write(file_data)
        file.close()
        #print("File has been received successfully")
        messagebox.showinfo("Success","Data has been received successfully")


    ##### icon #######
    image_icon2=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\WeTransfer.png")
    main.iconphoto(False,image_icon2)

    Hbackground=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\receiver.png")
    Label(main,image=Hbackground).place(x=-2,y=0)

    logo=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\account.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=10,y=250)

    Label(main,text="Receive",font=("arial",20),bg="#f4fdfe").place(x=90,y=273)

    Label(main, text="Input sender id:", font=("arial",10,"bold"),bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry (main, width=25, fg="black",border=0,bg="white" ,font=("arial", 15))
    SenderID.place (x=20,y=370)
    SenderID.focus()
    Frame(main,width=278,height=2,bg="black").place(x=20,y=395)

    Label (main, text="Filename for the incoming file:", font=("arial",10,"bold"),bg="#f4fdfe").place(x=20,y=420)
    incoming_file = Entry (main, width=25, fg="black",border=0,bg="white" ,font=("arial", 15))
    incoming_file.place (x=20,y=450)
    Frame(main,width=278,height=2,bg="black").place(x=20,y=475)

    
    imageicon=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",border=0,command=receiver)
    rr.place(x=20,y=500)

    main.mainloop()

root=Tk()
root.title("WeTransfer")
root.geometry("590x560+500+100")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

#### icon ####
image_icon=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\WeTransfer.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=("Acumin Variable Concept",20,"bold"),bg="#f4fdfe").place(x=30,y=35)

Frame(root,width=535,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\send.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,activebackground="#f4fdfe",command=Send)
send.place(x=85,y=105)

receive_image=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\receive.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0,activebackground="#f4fdfe",command=Receive)
receive.place(x=380,y=110)

#label
Label(root,text="Send",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=130,y=200)
Label(root,text="Receive",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=377,y=200)

background=PhotoImage(file=r"C:\Users\Rishabh Jain\OneDrive\Desktop\Python Programming\File Sharing App\Images\Background.png")
Label(root,image=background).place(x=-2,y=265)
root.mainloop()
