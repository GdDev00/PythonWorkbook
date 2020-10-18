
num = int(input("Inserisci il numero da convertire: "))
result=""
q = num
r = q%2
result= str(r) + result
q = q//2

while q>0:
    r = q%2
    result= str(r) + result
    q = q//2

print(result)