import random
# from generatepassword import *


# word=genpass(convo)

def password_encrypted(word):
    shift=random.randint(10,15)
    encrypt='' 
    for i in word:
        x=(ord(i)-shift)
        encrypt+=chr(x)
    encrypt+=chr(96+shift)
    return encrypt

def name_encrypt(word):
    new =''
    for i in word:
        x=ord(i)-97
        x+=100
        x%=26
        x+=97
        new+=chr(x)
    return new
# print("the encrypted password: ",encrypt)
