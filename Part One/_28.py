airTemp = float(input("Inserisci la temperatura dell'aria: "))
windSpeed = float(input("Inserisci la velocità del vento: "))

WCI = 13.12 + (0.6215*airTemp) - (11.37*(windSpeed**0.16)) + (0.3965*airTemp*(windSpeed**0.16))

print("WCI:{0}".format(WCI))

