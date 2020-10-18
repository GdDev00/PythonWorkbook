day = int(input("Inserisci il giorno: "))
month = int(input("Inserisci il mese: "))
year = int(input("Inserisci l'anno: "))

nextDayYear = year
nextDayMonth = month
nextDayDate = day

def checkLeapYear(year):
    isLeapYear = False

    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0:
        isLeapYear = False 
    elif year % 4 == 0:
        isLeapYear = True 
    else:
        isLeapYear=False

    return isLeapYear



if month != 12:
	nextDayYear = year 
else:
	if day != 31:
		nextDayYear = year 
	else:
		nextDayYear = year + 1
		
#per i mesi che hanno 30 giorni
if month != 9 and month != 4 and month != 6 and month != 6 and month != 11:
	if day != 31:
		nextDayMonth = month
		nextDayDate = day + 1
	else:
		if month != 12:
			nextDayMonth = month + 1
		else:
			nextDayMonth = 1
		nextDayDate = 1
else:
	if day != 30:
		nextDayMonth = month 
		nextDayDate = day + 1
	else:
		if month != 12:
			nextDayMonth = month + 1
		else:
			nextDayMonth = 1
		nextDayDate = 1
		
if month == 2:
    isLeapYear= checkLeapYear(year)
        #febbraio
    if day == 28 or day == 29:
        if isLeapYear and day==28:
            nextDayMonth = month 
            nextDayDate = day + 1
        else:
            nextDayMonth = month + 1
            nextDayDate = 1
    else:
        nextDayMonth = month 
        nextDayDate = day + 1
        
print("La prossima data rispetto a quella inserita è: {}-{}-{}.".format(nextDayYear, nextDayMonth, nextDayDate))

