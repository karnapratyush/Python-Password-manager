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
    regis_btn["command"]=register
    login_btn["command"]=login
   

    screen.mainloop()
main_screen()


 