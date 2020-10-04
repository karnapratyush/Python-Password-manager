from tkinter import *
from generatepassword import *
from encrypt import *
from decrypt import *

# def check():


def showing():
    # global enc_usrname
    enc_usrname=name_encrypt(usrname)
    screen10=Toplevel(root)
    screen10.geometry("200x200")
    Label(screen10, text="Your saved passwords", font="Arial 10", bg="red").grid(row=0)
    f=open(f"{enc_usrname}.txt","r")
    a=f.readlines()
    for i in range(1,len(a)):
        wn,pas=(a[i][:-1]).split(" ")
        wn=decrypt_name(wn)
        print(wn)
        pas=decrypt_password(pas)
        print(pas)

        Label(screen10,text=wn, font="Arial 10", bg="red").grid(row=i,column=0)
        Label(screen10,text=pas, font="Arial 10", bg="red").grid(row=i,column=1)
    f.close()
    


    
    

    


def saved():
    # global enc_usrname
    enc_usrname=name_encrypt(usrname)
    f=open(f"{enc_usrname}.txt","a")
    global name
    name=name.get()
    name=name_encrypt(name)

    
    f.write(f"{name} {gen_pas}\n")
    f.close()
    screen9.destroy()
    a.delete(0,END)
    b.delete(0,END)
    c.delete(0, END)
    w.delete("1.0",END)
    Label(root, text="saved !", font="Arial 10", bg="red").pack()
    


def saving():
    global screen9
    screen9=Toplevel(root)
    screen9.geometry("200x200")
    Label(screen9,text="Enter the name of website/app", font="Arial 10", bg="red").pack()
    global name
    name=StringVar()
    Entry(screen9, textvariable=name).pack()
    Button(screen9, text="save", font="Arial 10",bg="red",command=saved).pack()



def get_info():
    # j=0
    # for i in root.winfo_children():
    #     # print(i)
    #     if "button2" in str(i):
    #         break
    #     j+=1
    # for i in range(j+1,len(root.winfo_children())):
    #     root.winfo_children()[i].delete("1.0",END)
    w.delete("1.0",END)
    print(length_of_password.get())
    print(special_characters.get())
    print(other_chars.get())
    print(other_special.get())
    global gen_pas
    gen_pas=genpass(int(length_of_password.get()),special_characters.get(),other_special.get(),other_chars.get())
    gen_pas=password_encrypted(gen_pas)
    w.insert(1.0, gen_pas)
    w.pack()
   
    a.delete(0,END)
    b.delete(0,END)
    c.delete(0, END)



def after_login_screen(user):
    global usrname
    usrname=user

    global root 
    root=Tk()
    root.geometry("900x600")
    root.title(f"Welcome {user}")
    root["bg"]="lightsteelblue1"
     
    f1=Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
    f1.pack(side=LEFT, fill=Y)
    l=Label(f1,text="", font="Arial 10", bg="red")
    l.pack()
    l2=Label(f1,text="OPTIONS", font="Helvetica 16 bold",bg="red")
    l2.pack()
    global length_of_password
    global special_characters
    global other_chars
    length_of_password=StringVar()
    Label(f1,text="Enter the length of password", font="arial 10 ",bg="red").pack()
    global a
    a=Entry(f1, textvariable=length_of_password)
    a.pack()
    global b
    Label(f1,text="Enter the special characters required.\n Leave empty if not such specification", font="Arial 10",bg="red").pack()
    
    special_characters=StringVar()
    global c
    c=Entry(f1, textvariable=special_characters)
    c.pack()
    Label(f1,text="Do you want another special characters other than specified?", font="Arial 10",bg="red").pack()
    global other_special
    other_special=IntVar()
    Radiobutton(f1, text="Yes",font="Arial 10",bg="red", variable=other_special, value=1 ).pack()
    Radiobutton(f1, text="No",font="Arial 10",bg="red", variable=other_special, value=2 ).pack()
    Label(f1,text="If you want to add some more characters you can write below.\n Leave empty if not want to do so", font="Arial 10",bg="red").pack()
    other_chars=StringVar()
    b=Entry(f1, textvariable=other_chars)
    b.pack()
    # Button(f1, text="Submit", font="Arial 10",bg="red",command=get_info).pack()







    
    
    # f2=Frame(root, bg="grey",borderwidth=10,relief=SUNKEN,height=400, width=600)
    # f2.pack(side=LEFT, fill=X)
    
    # l_2=Label(f2,text="project tkinter-Pycharm", font="Helvetica 16 bold")
    # l_2.pack()
    # l2=Label(f2,text="project tkinter-Pycharm", font="Helvetica 16 bold")
    # l2.pack()
    # # Label(f1,text="OPTIONS").pack()
    Label(root,text="project tkinter-Pycharm", font="Helvetica 16 bold", pady=10).pack()
    Label(root,text="", font="Helvetica 16 bold").pack()
    Button(root, text="Generate Another", font="Arial 10",bg="red", pady=10,command=get_info).pack()
    Label(root,text="", font="Helvetica 16 bold").pack()
    Button(root, text="    Save    ", font="Arial 10",bg="red",  pady=10, command=saving).pack()
    Label(root,text="", font="Helvetica 16 bold").pack()
    Button(root, text="See Saved password", font="Arial 10",bg="red", pady=10, command=showing).pack()
    Label(root,text="", font="Helvetica 16 bold").pack()
    global w
    w = Text(root, height=2,state=NORMAL,width=10)
    w.insert("1.0", "")
    w.pack()
    f2=Frame(root,bg="red",borderwidth=6,relief=SUNKEN)
    f2.pack(side=LEFT, fill=X)
    ll=Label(f2,text="apple", font="Arial 10", bg="red")
    ll.pack()


    root.mainloop()

# after_login_screen("pratyush")