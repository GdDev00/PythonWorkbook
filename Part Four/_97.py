from tkinter import Tk
import random 
import pyperclip 
import sys

def calcolaPassword():
    password = []
    #genero lunghezza password casuale, da 7 a 10 caratteri max
    lenght = random.randint(7,10)

    i = 0
    while i<=lenght:
        password.append(chr(random.randint(33,126)))
        i = i+1

    string_ints = [str(int) for int in password]
    s =""
    return(s.join(string_ints))

def checkPassword(password):
    up_char = 0
    lower_char = 0
    number = 0
    #la password deve avere almeno 8 caratteri
    if(len(password)>=8):
        for i in range(0,len(password)-1):
            if(password[i].isdigit()==True):
                number+=1
            else:
                if(password[i].isupper()==True):
                    up_char+=1
                else:
                    lower_char+=1
    else:
        return False

    if(up_char>0 and lower_char>0 and number>0):
        return True
    else:
        return False

def main():
    count = 0
    result = False
    password = ""
    while result == False:
        password = calcolaPassword()
        result=checkPassword(password)
        count += 1

    print("La password è: %s" %password)
    print("Sono stati necessari %.d tentativi per generare una password sicura"%count)
    print("")
    print("LA PASSWORD E' STATA COPIATA NEGLI APPUNTI DI WINDOWS!")

    #modifica personale, cosi facendo la password salvata viene salvata negli appunti di windows
    #comodo per generare rapidamente una password da utilizzare online
    pyperclip.copy(password) 
    exit()

main()