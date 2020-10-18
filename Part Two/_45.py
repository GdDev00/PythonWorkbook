
BLACK_PLACE = "aceg"

coordinates = input("Inserisci la posizione della pedina sulla scacchiera: ")

col = coordinates[0].lower()
row = int(coordinates[1])

colStartsWhite = False
white = False

if col in BLACK_PLACE:
	colStartsWhite = False
else:
	colStartsWhite = True
	
	
if colStartsWhite == False:
	if row % 2 == 0:
		white = True
	else:
		white = False
else:
	if row % 2 == 0:
		white = False
	else:
		white = True
		
if white:
	print("La posizione è bianca.")
else:
	print("La posizione è nera.")
