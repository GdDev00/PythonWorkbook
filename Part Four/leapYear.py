year =  int(input("Inserisci l'anno: "))

is_leap_year = False

if year % 400 == 0:
	is_leap_year = True
elif year % 100 == 0:
	is_leap_year = False 
elif year % 4 == 0:
	is_leap_year = True 
else:
    is_leap_year = False 

if is_leap_year:
	print("E' un anno bisestile")
else:
	print("Non è un anno bisestile")

