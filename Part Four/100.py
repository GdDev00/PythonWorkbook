def isLeapYear(year):
    is_leap_year = False
    if year % 400 == 0:
        is_leap_year = True
    elif year % 100 == 0:
        is_leap_year = False 
    elif year % 4 == 0:
        is_leap_year = True 
    else:
        is_leap_year = False 

    return is_leap_year

def days_in_month(month, year): 
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    feb = 2
    
    if month in days_31: 
        print("Questo mese ha 31 giorni")
    elif month in days_30: 
        print("Questo mese ha 30 giorni")
    elif month == feb: 
        if isLeapYear(year): 
            print("Questo mese ha 29 giorni")
        else: 
            print("Questo mese ha 28 giorni")

anno = int(input("Inserisci anno (formato yyyy): "))
mese = int(input("Inserisci mese (formato mm): "))
days_in_month(mese,anno)