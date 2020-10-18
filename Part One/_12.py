#distanza tra due punti sulla terra

import math

HEART_AVERAGE_RADIUS_KM = 6371.01

t1 = float(input("Inserisci la coordinata x di un punto sulla terra: "))
t2 = float(input("Inserisci la coordinata y di un punto sulla terra:: "))

g1 = float(input("Inserisci la coordinata x di un secondo punto sulla terra: "))
g2 = float(input("Inserisci la coordinata y di un secondo punto sulla terra:: "))

distance = HEART_AVERAGE_RADIUS_KM * math.acos(math.sin(math.radians(t1)) * math.sin(math.radians(g1)) + \
math.cos(math.radians(t1)) * math.cos(math.radians(g1)) * math.cos(math.radians(t2-g2)))

print("La distanza tra i due punti è di %.4f km" %distance)

