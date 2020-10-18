PI_GRECO = 3.14

radius = float(input("Inserisci il raggio del cilindro: "))
height = float(input("Inserisci l'altezza del cilindro: "))

volume = PI_GRECO * (radius**2) * height

print("The volume of this cylinder is {0:.01f} units cubed.".format(volume))

