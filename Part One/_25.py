#conversione da n. secondi a formato d/h/m/s
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


totalSeconds = int(input("Inserisci il numero di secondi: "))

days = totalSeconds // SECONDS_IN_DAY
totalSeconds = totalSeconds % SECONDS_IN_DAY

hours = totalSeconds // SECONDS_IN_HOUR
totalSeconds = totalSeconds % SECONDS_IN_HOUR

minutes = totalSeconds // SECONDS_IN_MINUTE
totalSeconds = totalSeconds % SECONDS_IN_MINUTE

print("D:H:M:S : {:d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, totalSeconds))

