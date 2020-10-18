

dbLevel = float(input("Inserisci un livello in dB: "))

if dbLevel < 40:
	print("è molto silenzioso")
elif dbLevel > 130:
	print("c'è moltissimo rumore")
	
	
if dbLevel > 40:
	print("è tra il suono di una stanza calma e di una sveglia")
elif dbLevel > 70:
	print("è tra il suono di una sveglia e di un tosaerba")
elif dbLevel > 106:
	print("è tra il suono di un toaserba e di un martello pneumatico")
	
if dbLevel == 40:
	print("è una stanza tranquilla")
elif dbLevel == 70:
	print("è una sveglia")
elif dbLevel == 106:
	print("è un tosaerba")
elif dbLevel == 130:
	print("è un martello pneumatico")

