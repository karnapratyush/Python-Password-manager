
import random

# lower_case=[]
# for i in range(97,123):
#     lower_case.append(i)

# upper_case=[]
# for i in range(65,91):
#     upper_case.append(i)


# numbers=[]
# for i in range(48,58):
#     numbers.append(i)
# likely_punctuations=[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 61, 63, 64, 91, 93, 94, 95, 96, 123, 124, 125, 126]
# convo=[]
# #  adding a ovio capital letter

# convo.append(chr(random.randint(65,91)))

# #  same for small letter
# convo.append(chr(random.randint(97,123)))
# #  adding number
# convo.append(chr(random.randint(48,58)))


def genpass(n,schrs, mschrs, adchrs):
    lower_case=[]
    for i in range(97,123):
        lower_case.append(i)

    upper_case=[]
    for i in range(65,91):
        upper_case.append(i)


    numbers=[]
    for i in range(48,58):
        numbers.append(i)
    likely_punctuations=[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 61, 63, 64, 91, 93, 94, 95, 96, 123, 124, 125, 126]
    convo=[]
    #  adding a ovio capital letter

    convo.append(chr(random.randint(65,91)))

    #  same for small letter
    convo.append(chr(random.randint(97,123)))
    #  adding number
    convo.append(chr(random.randint(48,58)))


    convo+=list(schrs)
    convo+=list(adchrs)
    if mschrs==1:
        all_char=likely_punctuations+lower_case+upper_case+numbers
    else:
        all_char=lower_case+upper_case+numbers
    random.shuffle(all_char)
    left_length=n-len(convo)
    for i in range(left_length):
        convo.append(chr(all_char[i]))
    
    random.shuffle(convo)
    print("".join(convo))
    return "".join(convo)
    
        
        

       


