#converte un numero binario in decimale

def convertiInDecimale(binary):
    binary.replace(" ","")
    for char in binary:
        if char.isnumeric():
            num=int(char)

        else:
            print("Il testo inserito non è valido!")
            return -1

    lenght = len(binary)-1
    count = lenght
    somma=0
    while count>=0:
        if binary[count].isdecimal():
            num = int(binary[count])
            somma += num*(2**((count - lenght) *-1))
        else:
            print("Il testo inserito non è valido!")
            break
        count = count -1
        
    return somma


binary = input("inserisci un numero binario: ")
while binary!="":
    print(convertiInDecimale(binary))

    binary = input("inserisci un numero binario: ")
