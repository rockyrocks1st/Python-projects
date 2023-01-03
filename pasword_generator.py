#This program creates an 8-character password with numbers, symbols and upper and lower case letters

import random

password_length = 8

#Generate the 8 characters
password = ""
for i in range(password_length):
    rand_char = random.randint(0,3)
    if rand_char == 0:
        rand_letter = chr(random.randint(97,122)) #generate random lowercase letter
        password += rand_letter
    elif rand_char == 1:
        rand_letter = chr(random.randint(65,90)) #generate random uppercase letter
        password += rand_letter
    elif rand_char == 2:
        rand_number = chr(random.randint(48,57)) #generate random number
        password += rand_number
    elif rand_char == 3:
        rand_symbol = chr(random.randint(33,47)) #generate random symbol
        password += rand_symbol

print("Your password is: " + password)