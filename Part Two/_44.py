month = int(input("Inserisci mese (formato 1-12): "))
date = int(input("Inserisci il giorno: "))

holiday = ""

if month == 1 or month == 4 or month == 12:
	if month == 1 and date == 1:
		holiday = "New Year's Day"
	elif month == 4 and date == 1:
		holiday = "Canada Day"
	elif month == 12 and date == 25:
		holiday = "Christmas Day"
		
if holiday == "":
	print("Non c'è nessuna festa in questa data!")
else:
	print(holiday)


