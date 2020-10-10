from tkinter import *
from initial_screen import *
import time


sleep_time=5

attempt=0



def getvals_login():
    global sleep_time
    j=0
    for i in screen2.winfo_children():
        # print(i)
        if "button" in str(i):
            break
        j+=1
    for i in range(j+2,len(screen2.winfo_children())):
        screen2.winfo_children()[i].grid_forget()
    global root
    # print(uservalue_login.get())
    # print(passvalue_login.get())
    login_username=uservalue_login.get()
    login_password=passvalue_login.get()
    
    if len(login_username)==0:
        Label(screen2,text="username cannot be empty",font=("arial", 10, "italic"),fg="red",bg="wheat1").grid(row=5)
        return None
    elif len(login_password)==0:
        Label(screen2,text="Password field cannot be empty",font=("arial", 10, "italic"),fg="red",bg="wheat1").grid(row=5)
        return None
    # print("q")

    # login_password=dehash(login_password,x)
    
    global attempt
    # print(attempt)
   
    try:
        encrypt_login_user=name_encrypt(login_username)
        # print(encrypt_login_user)
        f=open(f"{encrypt_login_user}.txt","r")
        paswrd=f.readline()[:-1]

        f.close()
        given_password=dehash(login_password,paswrd)
        # print(given_password)
        # print(paswrd)
        username_dict[login_username]=paswrd

        if given_password==paswrd[:-3]:
            Label(screen2,text=f"Login Successful. Opening new tab",padx=15,pady=15,bg="wheat1",font=("arial", 10,"bold" ,"italic"),fg="Green").grid(row=5)
            sleep_time=5
            

           
            screen2.destroy()
            screen.destroy()
            after_login_screen(login_username)

        else:
            attempt+=1
            print("x")
            Label(screen2,text=f"Invalid  username/password. {3-attempt} remaining",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").grid(row=5)
            userentry_login.delete(0,END)
            passentry_login.delete(0,END)
        
            if attempt==3:
                messagebox.showinfo(" Login limit exceeded","Login Limit exceeded. Closing all windows!")
                screen2.destroy()
                time.sleep(2)
                screen.destroy()
                time.sleep(sleep_time)
                    


    except:
        attempt+=1

        Label(screen2,text=f"Invalid except  username/password. {3-attempt} remaining",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").grid(row=5)
        userentry_login.delete(0,END)
        passentry_login.delete(0,END)

        if attempt==3:
            
            # screen2.destroy()
            # screen3=Toplevel(screen2)
            # screen3.geometry("300x100")
            # Label(screen3,text="Maximum attempt reached. Closing              ",padx=15,pady=15,bg="wheat1",font=("arial", 10, "italic"),fg="red").pack()
            messagebox.showinfo(" Login limit exceeded","Login Limit exceeded. Closing all windows!")
            screen2.destroy()
            time.sleep(2)
            screen.destroy()
            time.sleep(sleep_time)
    










def login():
    global screen2
    screen2=Toplevel(screen,bg="wheat1")
    screen2.title("ZA@P Login")
    screen2.geometry("500x300")
    regis_btn["state"]="disabled"
    login_btn["state"]="disabled"
    Label(screen2,text="LOGIN",padx=15,pady=15,bg="wheat1",font=("arial", 12, "bold")).grid(row=0,column=1)
    Label(screen2,text="Enter the username**",padx=15,pady=15,bg="wheat1").grid(row=1,column=0)
    Label(screen2, text="Enter the password**",padx=15,pady=15,bg="wheat1").grid(row=2, column=0)

    global uservalue_login
    global passvalue_login
    global userentry_login
    global passentry_login
    global sleep_time
    sleep_time+=10
    
    uservalue_login=StringVar()
    passvalue_login=StringVar()
    
    userentry_login=Entry( screen2,textvariable=uservalue_login)
    passentry_login=Entry(screen2, textvariable=passvalue_login)
    userentry_login.grid(row=1, column=1)
    passentry_login.grid(row=2, column=1)
    
    bt=Button(screen2,text="Submit",command=getvals_login).grid(row=3, column=1)
    Label(screen2, text="** All fields are necessary",padx=15,pady=15,bg="wheat1").grid(row=4, column=0)
