month = int(input("Inserisci in numero il tuo mese di nascita: "))
day = int(input("Inserisci in numero il tuo giorno di nascita: "))

zodiacSign = ""

if (month == 12 and day >= 22) or (month == 1 and day <= 19):
	zodiacSign = "Capricorno"
	
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
	zodiacSign = "Acquario"
	
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
	zodiacSign = "Pesci"
	
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
	zodiacSign = "Ariete"
	
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
	zodiacSign = "Toro"

elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
	zodiacSign = "Gemini"
	
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
	zodiacSign = "Cancro"
	
elif (month == 7 and day <= 23) or (month == 8 and day <= 22):
	zodiacSign = "Leone"
	
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
	zodiacSign = "Vergine"
	
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
	zodiacSign = "Libra"
	
elif (month == 10 and day <= 23) or (month == 11 and day <= 21):
	zodiacSign = "Scorpione"
	
elif (month == 11 and day <= 22) or (month == 12 and day <= 21):
	zodiacSign = "Sagittario"
	
print(zodiacSign)

