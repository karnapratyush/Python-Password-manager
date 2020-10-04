from tkinter import *
def getvals_login():
    print(uservalue_login.get())
    print(passvalue_login.get())
    userentry_login.delete(0,END)
    passentry_login.delete(0,END)
