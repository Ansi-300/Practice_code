# Code Encrypted in Python


import random 
import string

char = ' ' + string.ascii_letters + string.digits + string.punctuation

char  = list(char)

key = char.copy()
random.shuffle(key)

# print (f"Char: {char}")
# print (f"Key : {key}")


plain_text  = input ("Enter a Text to enrrypted: ")

chiper = ''



for letter in plain_text :
    index = char.index(letter)
    chiper += key [index]


print (f"Orginal message : {plain_text}")
print(f"Encrypted message : {chiper}")



# decrypted_message 


chiper  = input ("Enter a Text to enrrypted: ")

decrypted_message = ''



for letter in chiper :
    index = key.index(letter)
    decrypted_message += char [index]




print(f"Encrypted message : {chiper}")
print (f"Orginal message : {decrypted_message}")