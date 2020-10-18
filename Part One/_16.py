PI_GRECO = 3.14

r = float(input("Inserisci un raggio r in cm: "))

area = PI_GRECO * (r**2)
vol = (4/3) * PI_GRECO * (r**3)

print("L'area del cerchio è di {0} cm.".format(area))
print("Il volume della sfera è di {0} cm2.".format(vol))

