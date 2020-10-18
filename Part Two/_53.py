UNACCEPTABLE = 0.0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6

value = float(input("Inserisci un valore per le prestazioni del dipendente: "))

descriptor = ""

if value == UNACCEPTABLE:
	descriptor = "Prestazioni inaccettabili"
elif value == ACCEPTABLE:
	descriptor = "Prestazioni accettabili"
elif value >= MERITORIOUS:
	descriptor = "Prestazione meritevole"

if descriptor != "":
    print("Il dipendente ha dimostrato una prestazione '{}'".format(descriptor))
    print("")
    print("Riceverà un aumento di € %.2f" %(value*2400.00))
else:
	print("Il valore inserito non è valido!")

