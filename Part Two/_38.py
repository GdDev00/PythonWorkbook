#mostra i giorni del mese inserito

month = input("Inserisci il nome del mese: ").lower()

if month == "settembre" or month == "aprile" or month == "giugno" or month == "novembre":
	print("Ci sono 30 giorni in questo mese.")
elif month == "febbraio":
	print("Ci sono 28 o 29 giorni in questo mese.")
else:
	print("Ci sono 31 giorni in questo mese.")

