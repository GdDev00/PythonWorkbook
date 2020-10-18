#conversione anni umani/anni cane

humanYearsOld = int(input("Inserisci il numero di anni: "))

#se il numero di anni è negativo restituisco 0
if humanYearsOld <= 0:
    humanYearsOld = 0
	
if humanYearsOld <= 2:
	dogYears = humanYearsOld * 10.5
elif humanYearsOld > 2:
	dogYears = 2 * 10.5
	dogYears += (humanYearsOld-2) * 4

if humanYearsOld == 0:
	print("Insersci un numero maggiore di 0!")
else:
	print("L'eta del cane è di: {0} anni animale".format(dogYears))

