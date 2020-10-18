import random 

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

inp = input("Premi invio per calcolare la password: ")
print(calcolaPassword())

