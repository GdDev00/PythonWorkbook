#nome di un triangolo

s1 = float(input("Inserisci la lunghezza del 1° lato del triangolo in cm: "))
s2 = float(input("Inserisci la lunghezza del 2° lato del triangolo in cm: "))
s3 = float(input("Inserisci la lunghezza del 3° lato del triangolo in cm: "))

triangleType = ""

if s1 == s2 == s3:
	triangleType = "equilatero"
elif s1 == s2 or s1 == s3 or s2 == s3:
	triangleType = "isoscele"
else:
	triangleType = "scaleno"
	
print("è un triangolo {}".format(triangleType))

