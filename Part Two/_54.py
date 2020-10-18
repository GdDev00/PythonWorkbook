wavelength = int(input("Immettere un valore per una lunghezza d'onda della luce visibile in nanometri: "))

colour = ""

if wavelength >= 350 and wavelength < 450:
	colour = "Viola"
elif wavelength >= 450 and wavelength < 495:
	colour = "Blue"
elif wavelength >= 495 and wavelength < 570:
	colour = "Verde"
elif wavelength >= 570 and wavelength < 590:
	colour = "Gialla"
elif wavelength >= 590 and wavelength < 620:
	colour = "Arancione"
elif wavelength >= 620 and wavelength <= 750:
	colour = "Rossa"
	
if colour != "":
	print("Il colore dell'onda è: {}.".format(colour))
else:
	print("Questa lunghezza d'onda è al di fuori dello spettro della luce visibile")

