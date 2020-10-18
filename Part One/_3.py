#CALCOLA L'AREA DI UNA STANZA

#richiedeo all'utente la larghezza e lunghezza della stanza in cm
width = int(input("Inserisci la larghezza della stanza in cm: "))
length = int(input("Inserisci la lunghezza della stanza in cm: "))

#calcolo l'area
area = width * length

#stampo a video i risultati
print("")

#risultato in centimetri
print("L'area della stanza è di %.2f cm2" %area)
#risultato in metri
print("L'area della stanza è di %.2f m2" %(area/100))


