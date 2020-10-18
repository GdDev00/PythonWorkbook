
num1 = int(input("Inserisci 1° numero intero: "))
num2 = int(input("Inserisci 2° numero intero: "))
d=0

d=min(num1,num2)

while num1%d !=0 and num2%d!=0:
    d = d-1

print(d)