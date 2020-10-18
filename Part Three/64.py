PENNIES_FOR_NICKEL = 5

line = input("Inserisci prezzo articolo (invio per uscire): ")
totalPrice = 0.0

while(line!=""):
    totalPrice +=float(line)
    line = input("Inserisci prezzo articolo (invio per uscire): ")

print("Il prezzo totale degli articoli è di $ %.2f" %totalPrice)

#calcolo il prezzo arrotondato
priceInPennies = totalPrice * 100
remainder = priceInPennies % PENNIES_FOR_NICKEL
	
if remainder > 2.5:
	priceInPennies += 5 - remainder 
else:
	priceInPennies -= remainder 
	
roundedPrice = priceInPennies * 0.01
rounded = roundedPrice

print("Pagando in contanti, il prezzo da pagare è di $: %.2f" %rounded)
