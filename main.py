from tkinter import *
from encrypt import *
import time
from hashing import *
from decrypt import *

from aflogin import *




attempt=0




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
        Label(screen1,text="**Username exist. Either login or use other username", padx=15,pady=2,bg="plum2", font=("arial", 10, "italic"),fg="red").grid(row=2,column=1)
    except:


        if len(username)==0 :
            a=Label(screen1,text="**Username cannot be empty!", padx=15,pady=2,bg="plum2", font=("arial", 10, "italic"),fg="red")
            a.grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            b.grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2")
            c.grid(row=6,column=1)
        elif len(password)==0:
            b=Label(screen1,text="**Password  cannot be empty!", padx=15,pady=2,bg="plum2", font=("arial", 10, "italic"),fg="red").grid(row=4,column=1)
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            c=abel(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=6,column=1)
        elif len(confirm_password)==0:
            c=Label(screen1,text="**Confirm Password  cannot be empty", padx=15,pady=2,bg="plum2", font=("arial", 10, "italic"),fg="red").grid(row=6,column=1)
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=4,column=1)

        elif password==confirm_password:
            Label(screen1,text="*Account created.\n Please login. \nClosing register window  ", padx=0,bg="plum2", font=("arial", 10, "italic"),fg="green").grid(row=9,column=0)
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
            screen1.after(5000, screen1.destroy) 
            username_dict[username]=1


        elif password!=confirm_password:
            a=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=2,column=1)
            b=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=4,column=1)
            c=Label(screen1,text="",padx=0,pady=2,bg="plum2").grid(row=6,column=1)
            
            Label(screen1,text="Password donot match. Please retry", padx=0,bg="plum2", font=("arial", 10, "italic"),fg="red").grid(row=9,column=0)


    userentry.delete(0,END)
    passentry.delete(0,END)
    confirmpassentry.delete(0,END)
    
    

















def register():
    global screen1

    screen1=Toplevel(screen,bg="plum2")
    screen1.title("Register")
    screen1.geometry("500x300")
    Label(screen1,text="",padx=15,pady=2,bg="plum2").grid(row=0,column=0)
    Label(screen1,text="USERNAME*",padx=15,pady=2,bg="plum2", font=("Times", 8, "bold")).grid(row=1,column=0)
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
    bt=Button(screen1,text="Submit",command=getvals_register).grid(row=8, column=1)
    








def getvals_login():
    j=0
    for i in screen2.winfo_children():
        # print(i)
        if "button" in str(i):
            break
        j+=1
    for i in range(j+1,len(screen2.winfo_children())):
        screen2.winfo_children()[i].grid_forget()
    global root
    # print(uservalue_login.get())
    # print(passvalue_login.get())
    login_username=uservalue_login.get()
    login_password=passvalue_login.get()
    
    if len(login_username)==0:
        Label(screen2,text="username cannot be empty",font=("arial", 10, "italic"),fg="red",bg="wheat1").grid(row=4)
        return None
    elif len(login_password)==0:
        Label(screen2,text="Password field cannot be empty",font=("arial", 10, "italic"),fg="red",bg="wheat1").grid(row=4)
        return None
    # print("q")

    # login_password=dehash(login_password,x)
    
    global attempt
    print(attempt)
   
    try:
        encrypt_login_user=name_encrypt(login_username)
        # print(encrypt_login_user)
        f=open(f"{encrypt_login_user}.txt","r")
        paswrd=f.readline()[:-1]

        f.close()
        given_password=dehash(login_password,paswrd)
        print(given_password)
        print(paswrd)
        username_dict[login_username]=paswrd

        if given_password==paswrd[:-3]:
            Label(screen2,text=f"Login Successful. Opening new tab",padx=15,pady=15,bg="wheat1",font=("arial", 10,"bold" ,"italic"),fg="Green").grid(row=4)
            

           
            screen2.destroy()
            screen.destroy()
            after_login_screen(login_username)

        else:
            attempt+=1
            print("x")
            Label(screen2,text=f"Invalid  username/password. {3-attempt} remaining",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").grid(row=4)
            userentry_login.delete(0,END)
            passentry_login.delete(0,END)
        
        if attempt==3:
            Label(screen2,text="Maximum attempt reached. Closing",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").grid(row=4)
            screen2
            time.sleep(15)


    except:
        attempt+=1
        print(attempt)
        print("y")

        Label(screen2,text=f"Invalid except  username/password. {3-attempt} remaining",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").grid(row=4)
        userentry_login.delete(0,END)
        passentry_login.delete(0,END)

        if attempt==3:
            Label(screen2,text="Maximum attempt reached. Closing",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").grid(row=4)
            screen2.after(5000, screen2.destroy()) 
            screen.destroy()
            time.sleep(5)
    










def login():
    global screen2
    screen2=Toplevel(screen,bg="wheat1")
    screen2.title("Login")
    screen2.geometry("500x300")
    Label(screen2,text="",padx=15,pady=15,bg="wheat1").grid(row=0,column=0)
    Label(screen2,text="Enter the username**",padx=15,pady=15,bg="wheat1").grid(row=1,column=0)
    Label(screen2, text="Enter the password**",padx=15,pady=15,bg="wheat1").grid(row=2, column=0)

    global uservalue_login
    global passvalue_login
    global userentry_login
    global passentry_login
    
    uservalue_login=StringVar()
    passvalue_login=StringVar()
    
    userentry_login=Entry( screen2,textvariable=uservalue_login)
    passentry_login=Entry(screen2, textvariable=passvalue_login)
    userentry_login.grid(row=1, column=1)
    passentry_login.grid(row=2, column=1)
    
    bt=Button(screen2,text="Submit",command=getvals_login).grid(row=3, column=1)
    















def main_screen():
    global screen
    global attempt
    attempt=0
    screen=Tk()
    screen["bg"]="rosybrown1"
    screen.geometry("600x300")
    screen.title("login/register")
    Label(text="Login/Register",width="300",height="2", font=("calibri",13),bg="rosybrown1").pack()
    Label(text="",bg="rosybrown1").pack()
    global username_array
    global username_dict
    username_dict={}
    f=open("usernames.txt","r")
    username_array=(f.read()).split('\n')
    for i in username_array[:-1]:
        username_dict[decrypt_name(i)]=1
    Button(text="login", height="2",width="30",command=login,bg="rosybrown1").pack()
    Label(text="",bg="rosybrown1").pack()
    Button(text="register", height="2",width="30",command=register,bg="rosybrown1").pack()

    screen.mainloop()
main_screen()