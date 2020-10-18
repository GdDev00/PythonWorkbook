#area di un poligono regolare

from math import tan, pi

s = float(input("Inserisci la lunghezza di ogni lato del poligono in cm: "))
n = float(input("Inserisci il numero dei lati del poligono: "))

area = (n * (s**2)) / (4 * tan(pi/n))

print("L'area del poligono è di {0:0.2f} cm2".format(area))

