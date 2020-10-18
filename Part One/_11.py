#convertitore miglia/galloni -> km/litri

MPG_LT_CONVERTER = 0.425143707

mpg = float(input("Inserisci miglia per gallone: "))

lt =  mpg * MPG_LT_CONVERTER 

print("La conversione l/100km è: %.2f" %lt)

