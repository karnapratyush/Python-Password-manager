
import random

#  the gen_pass will take length of password(n), if special characters given(schrs), do they want more special characters(mschrs) and if additional characters like abcd or 1234(adchrs)
def genpass(n,schrs, mschrs, adchrs):
    #  making an array of lower characters
    lower_case=[]
    for i in range(97,123):
        lower_case.append(i)

    #  making an array of upper characters
    upper_case=[]
    for i in range(65,91):
        upper_case.append(i)

    #  making an array of numbers from 0-9
    numbers=[]
    for i in range(48,58):
        numbers.append(i)
    likely_punctuations=[33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 61, 63, 64, 91, 93, 94, 95, 96, 123, 124, 125, 126]

    # making an array which will have the password characters
    password_array=[]

    #  adding a must capital letter

    password_array.append(chr(random.randint(65,91)))

    #  adding a must lower alphabet
    password_array.append(chr(random.randint(97,123)))

    #  adding a must number
    password_array.append(chr(random.randint(48,58)))

    #  adding the special characters provided by user in the array and also the additional letters if given
    password_array+=list(schrs)
    password_array+=list(adchrs)

    # if user wants more special characters then we will add that array otherwise will not add.
    if mschrs==1:
        all_char=likely_punctuations+lower_case+upper_case+numbers
    else:
        all_char=lower_case+upper_case+numbers

    #  shuffling and taking out  left characters from the all_char
    random.shuffle(all_char)
    left_length=n-len(password_array)
    for i in range(left_length):
        password_array.append(chr(all_char[i]))
    
    random.shuffle(password_array)
    # print("".join(password_array))
    return "".join(password_array)
    
        
        

       


