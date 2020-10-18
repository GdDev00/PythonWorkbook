VOWEL = "aeiou"

letter = input("Inserisci una lettera dell'alfabeto: ").lower()

print("")
if letter in VOWEL:
	print("{0} --> questa lettera è una VOCALE".format(letter))
else:
	print("{0} --> questa lettera è una CONSONANTE".format(letter))

