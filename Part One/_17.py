COSTO_ENERGIA = 8.9
JOULE_TO_KWH = 2.77778e-7

CAPACITA_TERMICA_ACQUA = 4.186

#l'acqua ha una densità pari a un 1.0 g per millilitro 

q = float(input("Inserisci la quantità d'acqua in millilitri: "))
t_Inc = float(input("Inserisci l'incremento di temperatura desiderato in °C: "))

j = q*t_Inc*CAPACITA_TERMICA_ACQUA

print("Per incrementare la temperatura di %.2f °C sono necessari %.2f J" %(t_Inc, j))

#converto i joule in kwh
kwh = j * JOULE_TO_KWH
print("Sono necessari %.4f kwh di energia elettrica per permetter il riscaldamento dell'acqua" %kwh)
print("Ipotizzando un costo dell'energia pari a 8.9 centesimi per Kwh, il costo per il riscaldamento è di € %.2f" \
    %(kwh*COSTO_ENERGIA))