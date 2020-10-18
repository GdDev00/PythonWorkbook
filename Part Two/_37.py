
noOfSides = int(input("Inserisci il numero dei lati della forma geometrica: "))

if noOfSides == 3:
	print("è un triangolo.")
elif noOfSides == 4:
	print("è un quadrato.")
elif noOfSides == 5:
	print("è un pentagono.")
elif noOfSides == 6:
	print("è un esagono.")
elif noOfSides == 7:
	print("è un settagono.")
elif noOfSides == 8:
	print("è un ottagono.")
elif noOfSides == 9:
	print("è un nonagono.")
elif noOfSides == 10:
	print("è un decagono")
else:
	print("Per favore, inserisci un intero con più di 2 lati!")

