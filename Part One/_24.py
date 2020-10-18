#conversione giorni/ore/minuti/secondi in secondi

giorni = int(input("Inserisci il numero di giorni: "))
ore = int(input("Inserisci il numero di ore: "))
minuti = int(input("Inserisci il numero di minuti: "))
secondi = int(input("Inserisci il numero di secondi: "))

totale = 0
totale += secondi
totale += (minuti*60)
totale += (ore*60**2)
totale += (giorni*60*60*24)

print("Il numero totale di secondi è {}.".format(totale))

