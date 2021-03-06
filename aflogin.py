from tkinter import *
from generatepassword import *
from encrypt import *
from decrypt import *

    

def yes():
    global dictionary
    dictionary[name.lower()]=gen_pas
    enc_usrname=name_encrypt(usrname)
    f=open(f"{enc_usrname}.txt","w")
    f.write(dictionary["password"]+'\n')
    for i in dictionary.keys():
        if i!="password":
            f.write(f"{name_encrypt(i)}\x0e{password_encrypted(dictionary[i])}\n")
    f.close()
    z.insert("1.0","password changed!")
    screen9.destroy()
    save_btnn["state"]="disabled"
    gen_btn["state"]="active"
    saved_pass_btn["state"]="active"


    
def no():
    screen9.destroy()
    w.delete("1.0",END)
    z.delete("1.0",END)
    save_btnn["state"]="disabled"
    gen_btn["state"]="active"
    saved_pass_btn["state"]="active"



def showing():
    enc_usrname=name_encrypt(usrname)
    length=len(dictionary)
    screen10=Toplevel(root)
    screen10.geometry(f"600x{length*30}")
    Label(screen10, text="Your saved passwords", font="Arial 10").grid(row=0)
    f=open(f"{enc_usrname}.txt","r")
    a=f.readlines()
    for i in range(1,len(a)):
        wn,pas=(a[i][:-1]).split(chr(14))
        wn=decrypt_name(wn)
        print(wn)
        pas=decrypt_password(pas)
        print(pas)
        zz = Text(screen10, height=1,state=NORMAL,width=20,fg="red")
        zz.insert("1.0", wn)
        zz.grid(row=i,column=0)
        zzz=Text(screen10, height=1,state=NORMAL,width=50,fg="red")
        zzz.insert("1.0", pas)
        zzz.grid(row=i,column=1)
    f.close()
    


    
    

    


def saved():
    enc_usrname=name_encrypt(usrname)
    
    global name
    global gen_pas
    global dictionary
    name=name.get()
    try:
        dictionary[name.lower()]
        sa["state"]="disabled"
        
        print(dictionary[name.lower()])
        global screen15
        screen15=Toplevel(screen9)
        screen15.geometry("420x50")
        Label(screen15,text="website name exist.Do you want to change password?", font="Arial 10").grid(row=1)
        Button(screen15,text="YES",bg="red", command=yes,width=10).grid(row=2,column=0)


        Button(screen15,text="NO",bg="red",command=no,width=10).grid(row=2,column=1)

    except:
        dictionary[name.lower()]=gen_pas
        name=name_encrypt(name)
         
        gen_pas=password_encrypted(gen_pas)

        f=open(f"{enc_usrname}.txt","a")
        f.write(f"{name}\x0e{gen_pas}\n")
        f.close()
        z.insert("1.0","saved")
        screen9.destroy()
        save_btnn["state"]="disabled"
        gen_btn["state"]="active"
        saved_pass_btn["state"]="active"

    
    
    


def saving():
    global screen9
    save_btnn["state"]="disabled"
    gen_btn["state"]="disabled"
    saved_pass_btn["state"]="disabled"

    screen9=Toplevel(root)
    screen9.geometry("200x80")
    Label(screen9,text="Enter the name of website/app", font="Arial 10").pack()
    global name
    name=StringVar()
    Entry(screen9, textvariable=name).pack()
    global sa
    sa=Button(screen9, text="save", font="Arial 10",bg="red",command=saved)
    sa.pack()
    sa["state"]="active"



def get_info():
    global gen_pas
    
    w.delete("1.0",END)
    z.delete("1.0",END)
    if len(writeselfpass.get())==0:
       
        
        if length_of_password.get()=='':
            z.insert(1.0," Both length of password and desired password cannot be empty ")
            save_btnn["state"]="disabled"
        elif int(length_of_password.get())<3:
            z.insert(1.0," Password length is less than 3 ")
            save_btnn["state"]="disabled"
            # z.tag_config( fg="red") 
        elif (int(length_of_password.get())-3-len(special_characters.get()))<len(other_chars.get()):
            z.insert(1.0,f" for a length of {length_of_password.get()} number of characters in specified words should be less than {(int(length_of_password.get())-3-len(special_characters.get()))}")
            save_btnn["state"]="disabled"
        else:
            gen_pas=genpass(int(length_of_password.get()),special_characters.get(),other_special.get(),other_chars.get())
            w.insert(1.0, gen_pas)
            w.pack()
            save_btnn["state"]="active"
   

    else:
        if len(e.get())<3:
            z.insert(1.0," Password length is less than 3 ")
            save_btnn["state"]="disabled"
        else:

            gen_pas=writeselfpass.get()

            w.insert(1.0, gen_pas)
            w.pack()
            save_btnn["state"]="active"
   
    specialchar_entry.delete(0,END)
    pas_entry.delete(0,END)
    otherchar_entry.delete(0, END)


#  creating a  new screen after correct login with the username

def after_login_screen(user):

    global usrname
    usrname=user

    #   writing basic geometry details
    global root 
    root=Tk()
    root.geometry("900x600")
    root.title(f" ZA@P Welcomes you,  {user}")
    root["bg"]="cadetblue3"
     
    #  dividing the screen in two frames

    f1=Frame(root,bg="cornsilk3",borderwidth=6,relief=SUNKEN)
    f1.pack(side=LEFT, fill=Y)
    l=Label(f1,text="", font="Arial 10", bg="cornsilk3")
    l.pack()
    l2=Label(f1,text="OPTIONS", font="Helvetica 16 bold",bg="cornsilk3")
    l2.pack()


    #  using global variables for each kind of conditions
    global length_of_password
    global special_characters
    global other_chars
    

    # password length initializing
    length_of_password=StringVar()
    Label(f1,text="Enter the length of password", font="arial 10 ",bg="cornsilk3").pack()

    global pas_entry
    pas_entry=Entry(f1, textvariable=length_of_password)
    pas_entry.pack()
    

    #  special character conditions
    Label(f1,text="Enter the special characters required.\n Leave empty if not such specification", font="Arial 10",bg="cornsilk3").pack()
    
    special_characters=StringVar()
    global specialchar_entry
    specialchar_entry=Entry(f1, textvariable=special_characters)
    specialchar_entry.pack()
    Label(f1,text="Do you want another special characters other than specified?", font="Arial 10",bg="cornsilk3").pack()

    #  other special characters requirement
    global other_special
    other_special=IntVar()
    Radiobutton(f1, text="Yes",font="Arial 10",bg="cornsilk3", variable=other_special, value=1 ).pack()
    Radiobutton(f1, text="No",font="Arial 10",bg="cornsilk3", variable=other_special, value=2 ).pack()
    Label(f1,text="If you want to add some more characters you can write below.\n Leave empty if not want to do so", font="Arial 10",bg="cornsilk3").pack()
    other_chars=StringVar()
    global otherchar_entry
    otherchar_entry=Entry(f1, textvariable=other_chars)
    otherchar_entry.pack()

    #  writing complete password 

    global writeselfpass_entry
    global writeselfpass
    writeselfpass=StringVar()
    Label(f1,text="", font="Arial 10",bg="cornsilk3").pack()
    Label(f1,text="Or if you wish you can write whole password ", font=("Arial","10","bold"),bg="cornsilk3").pack()

    writeselfpass_entry=Entry(f1, textvariable=writeselfpass)
    writeselfpass_entry.pack()


    #  reading writing all password of a person

    enc_usrname=name_encrypt(usrname)
    f=open(f"{enc_usrname}.txt","r")
    infos=f.readlines()
    f.close()
    global dictionary
    dictionary={}
    dictionary["password"]=infos[0][:-1]
    for i in range(1,len(infos)):
        wq,rf=(infos[i][:-1]).split(chr(14))
        wq=decrypt_name(wq)
        rf=decrypt_password(rf)
        dictionary[wq.lower()]=rf


    #  another half of screen
    Label(root,text="project tkinter-Pycharm", font="Helvetica 16 bold", pady=10,bg="cadetblue3").pack()
    Label(root,text="", font="Helvetica 16 bold",bg="cadetblue3").pack()

    global gen_btn
    gen_btn=Button(root, text="      Generate      ", font=("Calibri", "14"),bg="tan2", pady=10,command=get_info)
    gen_btn.pack()
    gen_btn["state"]="active"
    Label(root,text="", font="Helvetica 16 bold",bg="cadetblue3").pack()

    global save_btnn
    save_btnn=Button(root, text="       Save       ", font=("Calibri", "14"),bg="olivedrab2",  pady=10, command=saving)
    save_btnn.pack()
    save_btnn["state"]="disabled"
    Label(root,text="", font="Helvetica 16 bold",bg="cadetblue3").pack()


    global saved_pass_btn
    saved_pass_btn=Button(root, text="See Saved password", font=("Calibri", "14"),bg="lightpink", pady=10, command=showing)
    saved_pass_btn.pack()
    saved_pass_btn["state"]="active"
    Label(root,text="", font="Helvetica 16 bold",bg="cadetblue3").pack()

    global w
    w = Text(root, height=2,state=NORMAL,width=40)
    w.insert("1.0", "")
    w.pack()
    global z
    Label(root,text="Errors", font="Helvetica 16 bold",bg="cadetblue3").pack()
    z = Text(root, height=2,state=NORMAL,width=50,fg="red")
    z.insert("1.0", "")
    z.pack()
    Label(f1,text="Notice", font="Helvetica 14 bold ",bg="cornsilk3", fg="red").pack()

    Label(f1,text="** Password length should be minimum of length 3. \n Username should start with a alphabet. \n If you want to enter a password it should be atleast 3 character long \nwith a Capital and small letter", font="Helvetica 10 ",bg="cornsilk3", fg="red").pack()


    

    root.mainloop()
