def checkLeapYear(year):
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
        return 31
    elif month in days_30: 
        return 30
    elif month == feb: 
        if checkLeapYear(year): 
            return 29
        else: 
            return 28

def isMagicDate (day,month,year):
    if(day * month == year %100):
        return True
    else:
        return False

def main():
    for year in range(1900, 2000):
        for month in range(1,13):
            for day in range(1, days_in_month(month,year) +1):
                if isMagicDate(day,month,year):
                    print("%02d/%02d/%04d è una data magica! "%(day,month,year))

main()