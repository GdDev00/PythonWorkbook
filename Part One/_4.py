
#DATI LARGHEZZA E LUNGHEZZA DI UNA FATTORIA IN PIEDI, 
#VISUALIZZA L'AREA IN ACRI

FEET_IN_ACRE = 43560

width = int(input("Inserisci la larghezza del terreno in piedi: "))
length = int(input("Inserisci la lunghezza del terreno in piedi: "))

area = (width * length) / FEET_IN_ACRE

print("L'area del terreno è di %.2f acri" %area)
