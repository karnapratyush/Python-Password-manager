
def decrypt_password(word):
    decrypted_word=''
    key=ord(word[-1])-96
    for i in word[:-1]:
        x=(ord(i)+key)
        decrypted_word+=chr(x)
    return decrypted_word

def decrypt_name(word):
    original=''
    for i in word:
        x=ord(i)-97
        x-=100
        x%=26
        x+=97
        original+=chr(x)
    return original
