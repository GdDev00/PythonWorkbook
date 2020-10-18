import math

l1 = float(input("Inserisci il 1° lato del triangolo in cm: "))
l2 = float(input("Inserisci il 2° lato del triangolo in cm: "))
l3= float(input("Inserisci il 3° lato del triangolo in cm: "))

s = (l1+l2+l3) / 2

area = math.sqrt(s * (s-l1) * (s-l2) * (s-l3))

print("L'area del triangolo è di {0:0.2f} cm2.".format(area))

