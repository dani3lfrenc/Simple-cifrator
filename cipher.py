from typing import final, get_args

import time
from time import *



# ------------------------------------------------------------------------

# Definizione della funzione per decriptare

def decript():
    code_to_cifrate = input("\nEnter the text you want to decrypt: ")

    code_to_cifrate_list = list(code_to_cifrate)


    cifrate_list = list("abcdefghijklmnopqrstuvwxyz @#")
    final_code = ""

    i2 = 0 

# Insert where there is the numeber 2, the key you would use, example: 3 ==> the cifrator goes 3 position forward

    for i in code_to_cifrate_list:
        new_pos = cifrate_list.index(i)-2
        final_code = final_code + cifrate_list[new_pos]
        i2 = i2 + 1
    
    sleep(2)

    print("\n"+final_code+"\n")

# ------------------------------------------------------------------------

# Definizione della funzione per criptare i file

def cript():
    cifrate_code = input("\nEnter the text you want to encrypt: ")

    cifrate_code_list = list(cifrate_code)


    cifrate_list = list("abcdefghijklmnopqrstuvwxyz @#")
    final_code = ""
    
    i2 = 0

    for i in cifrate_code_list:
        new_pos = cifrate_list.index(i)+2
        final_code = final_code + cifrate_list[new_pos]
        i2 = i2 + 1
    
    sleep(2)

    print("\n"+ final_code+"\n")
    
# ------------------------------------------------------------------------
    

# Definizione dell'input dell'utente


choose = input("Press 1 to decrypt, press 2 to encrypt or 3 to exit: ")

if choose ==  "1":

    decript()

elif choose == "2":

    cript()
    
elif choose == "3":

        quit()


