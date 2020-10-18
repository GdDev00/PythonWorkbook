from math import sqrt

perimeter = 0

x1 = float(input("Inserisci la coordinata X: "))
y1 = float(input("Inserisci la coordinata Y: "))

prev_x = x1
prev_y = y1

line = input("Inserisci la coordinata X (spazio per uscire): ")

while line !="":
    x2 = float(line)
    y2 = float(input("Inserisci la coordinata Y (spazio per uscire): "))
    dist = (sqrt((prev_x - x2) **2 + (prev_y - y2)**2))
    perimeter = perimeter + dist
    prev_x = x2
    prev_y = y2
    line = input("Inserisci la coordinata X (spazio per uscire): ")


print()
print("Il perimetro del poligono è di " + str(perimeter))
