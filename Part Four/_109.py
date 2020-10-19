
def calcolaNumeriDivisori(intero):
    divisori=[]
    i=intero-1
    while i>0:
        if intero % i == 0: #il numero divide perfettamente quel numero
            divisori.append(i)
        i=i-1

    return divisori


def main():
    num= int(input("Inserisci un numero intero: "))
    divisori = calcolaNumeriDivisori(num)
    for numero in divisori:
        print(numero)


if __name__ == "__main__":
    main()