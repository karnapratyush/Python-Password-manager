from tkinter import *
global screen
global attempt
attempt=0
screen=Tk()
screen["bg"]="rosybrown1"
screen.geometry("600x300")
screen.title("ZA@P ")
Label(text="Welcome To ZA@P Password Manager",width="300",height="2", font=("Arial",20, "bold", "italic"),bg="rosybrown1").pack()
Label(text=" To use our service either login or register",width="300",height="2", font=("Tempus Sans ITC",14),bg="rosybrown1",fg="blue").pack()
Label(text="",bg="rosybrown1").pack()
global  login_btn
global regis_btn
login_btn=Button(screen, text="login", height="2",width="30",bg="rosybrown1")
login_btn.pack()
Label(text="",bg="rosybrown1").pack()
regis_btn=Button(text="register", height="2",width="30",bg="rosybrown1")
regis_btn.pack()
