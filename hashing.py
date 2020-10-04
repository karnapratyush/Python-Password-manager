import random
from encrypt import *
def hash(word):
    x=random.randint(20,128)
    y=random.randint(20,128)
    z=random.randint(20,128)
    hashed=''
    for i in word:
        l=ord(i)
        p1=l**x  
        p1%=128
        p2=l**y
        p2%=128
        p3=int(l**z)
        p3%=128
        if p1==10:
            p1=100
        if p2==10:
            p2=100
        if p3==10:
            p3=100
        hashed+=chr(p1)
        hashed+=chr(p2)
        hashed+=chr(p3)
    hashed+=chr(x)
    hashed+=chr(y)
    hashed+=chr(z)

    
    
    return hashed




# f=open("w.txt","w")
# f.write(hash("Pratyush")+"\n")
# f.close()

# word=hash("pratyush")
# print(word)
# print(word[:-5])

def dehash(word,converted):
    z=ord(converted[-1])
    y=ord(converted[-2])
    x=ord(converted[-3])
    new_word=''
    for i in word:
        l=ord(i)
        p1=l**x
        p1%=128
        p2=l**y
        p2%=128
        p3=int(l**z)
        p3%=128
        if p1==10:
            p1=100
        if p2==10:
            p2=100
        if p3==10:
            p3=100
        new_word+=chr(p1)
        new_word+=chr(p2)
        new_word+=chr(p3)
    
    return new_word


        

