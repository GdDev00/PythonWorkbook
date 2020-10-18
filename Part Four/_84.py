def median (a,b,c):
    if a<b and b<c or a >b and b>c:
        return b
    if b <c and c<a or c>a and b>c:
        return c
    if b>a and a>c or b<a and a<c:
        return b

def main():
    a = float(input("Inserisci il 1° valore: "))
    b = float(input("Inserisci il 2 valore: "))
    c = float(input("Inserisci il 3° valore: "))

    print("la media è %.3f" %median(a,b,c))

main()