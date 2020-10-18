import math

ACCELLERAZIONE_GRAVITA = 9.8 #m/s2

def calcolaVelocita(initialSpeed, acceleration, distance):
    temp = (2 * acceleration * distance) + initialSpeed
    return math.sqrt(temp)


h_obj = float(input("Inserisci altezza (m) da cui l'oggetto dovrà cadere: "))

v = calcolaVelocita(0,ACCELLERAZIONE_GRAVITA, h_obj)

print("L'oggetto in caduta libera avrà una velocità di %.4f m/s" %v)

