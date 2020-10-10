from tkinter import *
from encrypt import *
import time
from hashing import *
from decrypt import *
from tkinter import messagebox
from aflogin import *
from initial_screen import *
from registerscreen import  *
from loginscreen import login




def main_screen():
    # global screen
    # global attempt
    # attempt=0
    # screen=Tk()
    # screen["bg"]="rosybrown1"
    # screen.geometry("600x300")
    # screen.title("ZA@P ")
    # Label(text="Welcome To ZA@P Password Manager",width="300",height="2", font=("Arial",20, "bold", "italic"),bg="rosybrown1").pack()
    # Label(text=" To use our service either login or register",width="300",height="2", font=("Tempus Sans ITC",14),bg="rosybrown1",fg="blue").pack()
    # Label(text="",bg="rosybrown1").pack()
    
    global username_array
    global username_dict
    username_dict={}
    f=open("usernames.txt","r")
    username_array=(f.read()).split('\n')
    for i in username_array[:-1]:
        username_dict[decrypt_name(i)]=1
    regis_btn["command"]=register
    login_btn["command"]=login
   

    screen.mainloop()
main_screen()


 