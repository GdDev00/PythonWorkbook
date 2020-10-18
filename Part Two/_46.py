
month = input("Inserisci il nome di un mese: ").lower()
day = int(input("Inserisci il numero di giorno del mese: "))

season = ""

spring = False
summer = False
fall = False
winter = False

if month == "marzo" or month == "aprile" or month == "maggio" or month == "giugno":
	if month == "marzo" and day >= 20:
		spring = True
		
	elif month == "aprile" or month == "maggio":
		spring  = True
		
	elif month == "giugno" and day < 21:
		spring = True
		
if month == "giugno" or month == "luglio" or month == "agosto" or month == "settembre":
	if month  == "giugno" and day >= 21:
		summer = True
		
	elif month == "luglio" or month == "agosto":
		summer = True
		
	elif month == "settembre" and day < 22:
		summber = True
		

if month == "settembre" or month == "ottobre" or month == "novembre" or month == "dicembre":
	if month == "september" and day >= 22:
		fall = True
		
	elif month == "ottobre" or month == "novembre":
		fall = True
		
	elif month == "dicembre" and day < 21:
		fall = True
		
if month == "dicembre" or month == "gennaio" or month == "febbraio" or month == "marzo":
	if month == "dicembre" and day >= 20:
		winter = True
		
	elif month == "gennaio" or month == "febbraio":
		winter = True
		
	elif month == "marzo" and day < 20:
		winter = True
		
if spring:
	print("La data cade in primavera.")
elif summer:
	print("La data cade in estate.")
elif fall:
	print("La data cade in autunno.")
elif winter:
	print("La data cade in inverno.")

