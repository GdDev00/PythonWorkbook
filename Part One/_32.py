a = int(input("Inserisci il 1° numero: "))
b = int(input("Inserisci il 2° numero: "))
c = int(input("Inserisci il 3° numero: "))

smallest = min(a, b, a)
largest = max(a, b, c)
middle = (a+b+c) - smallest - largest

print("{}, {}, {}.".format(smallest, middle, largest))

