from tkinter import *
from initial_screen import *
from encrypt import *
import time
from hashing import *
from decrypt import *
def getvals_register():
    
    username=uservalue.get()
    password=passvalue.get()
    confirm_password=confirmpass.get()
    # print(username)
    # print(password)
    # print(confirm_password)
    j=0
    for i in screen1.winfo_children():
        # print(i)
        if "button" in str(i):
            break
        j+=1
    for i in range(j+1,len(screen1.winfo_children())):
        screen1.winfo_children()[i].grid_forget()
        
    try:
        username_dict[username]
        Label(screen1,text="**Username exist. Either login or use other username", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red").grid(row=2,column=1)
    except:


        if len(username)==0 :
            a=Label(screen1,text="**Username cannot be empty!", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red")
            a.grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            b.grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            c.grid(row=6,column=1)
        elif len(password)==0:
            b=Label(screen1,text="**Password  cannot be empty!", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red").grid(row=4,column=1)
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=6,column=1)
        elif len(confirm_password)==0:
            c=Label(screen1,text="**Confirm Password  cannot be empty", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red").grid(row=6,column=1)
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=4,column=1)
        elif (ord(username[0])<65 or ord(username[0])>122) or (90<ord(username[0])<97):
            a=Label(screen1,text="**Username must start with a  alphabhet", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red")
            a.grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            b.grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            c.grid(row=6,column=1)
        elif len(username)<5:
            a=Label(screen1,text="**Username should be atleast 5 characters long!", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red")
            a.grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            b.grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2")
        elif len(password)<5:
            a=Label(screen1,text="*Password should be atleast 5 characters long!", padx=15,pady=2,bg="plum2", font=("arial", 8, "italic"),fg="red")
            a.grid(row=4,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            b.grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2")

        elif password==confirm_password:
            Label(screen1,text="*Account created.\n Please login. \nClosing register window  ", padx=0,bg="plum2", font=("arial", 10, "italic","bold"),fg="green").grid(row=9,column=0)
            f=open("usernames.txt","a")
            encrypt=name_encrypt(username)

            f.write(encrypt+'\n') 
            f.close()
            f=open(f"{encrypt}.txt","a")
            pass_encrypt=hash(password)
            f.write(pass_encrypt+'\n')
            f.close()
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=6,column=1)
            regis_btn["state"]="active"
            login_btn["state"]="active"
            screen1.after(2000, screen1.destroy) 
            username_dict[username]=1


        elif password!=confirm_password:
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=6,column=1)
            
            Label(screen1,text="Password donot match. Please retry", padx=0,bg="plum2", font=("arial", 8, "italic"),fg="red").grid(row=9,column=0)


    userentry.delete(0,END)
    passentry.delete(0,END)
    confirmpassentry.delete(0,END)
    
    












def register():
    global screen1
    regis_btn["state"]="disabled"
    login_btn["state"]="disabled"

    screen1=Toplevel(screen,bg="plum2")
    screen1.title("ZA@P Register")
    screen1.geometry("500x300")
    Label(screen1,text="",padx=15,pady=2,bg="plum2").grid(row=0,column=0)
    Label(screen1,text="USERNAME*",padx=15,pady=2,bg="plum2", font=("Calibri", 10, "bold")).grid(row=1,column=0)
    a=Label(screen1,text="",padx=15,pady=2,bg="plum2")
    a.grid(row=2,column=0)
    Label(screen1, text="PASSWORD*",padx=15,pady=2,bg="plum2", font=("Times", 8, "bold")).grid(row=3, column=0)
    b=Label(screen1,text="",padx=15,pady=2,bg="plum2")
    b.grid(row=4,column=0)
    Label(screen1, text="CONFIRM PASSWORD*",padx=15,pady=2,bg="plum2", font=("Times", 8, "bold")).grid(row=5, column=0)
    c=Label(screen1,text="",padx=15,pady=2,bg="plum2")
    c.grid(row=6,column=0)
    Label(screen1,text="* All fields are necessary",padx=15,pady=2,bg="plum2",font=("arial", 8, "italic")).grid(row=7,column=0)
    global uservalue
    global passvalue
    global confirmpass
    global userentry
    global passentry
    global confirmpassentry
    uservalue=StringVar()
    passvalue=StringVar()
    confirmpass=StringVar()
    
    userentry=Entry( screen1,textvariable=uservalue)
    passentry=Entry(screen1, textvariable=passvalue)
    userentry.grid(row=1, column=1)
    passentry.grid(row=3, column=1)
    confirmpassentry=Entry(screen1, textvariable=confirmpass)
    confirmpassentry.grid(row=5, column=1)
    global username_array
    global username_dict
    username_dict={}
    f=open("usernames.txt","r")
    username_array=(f.read()).split('\n')
    for i in username_array[:-1]:
        username_dict[decrypt_name(i)]=1
    f.close()
    
    bt=Button(screen1,text="Submit",command=getvals_register,height=2,width=10,bg="plum2").grid(row=8, column=1)



