
cents = int(input("Inserisci il numero di centesimi: "))

#toonie = 2$
toonies = int(cents / 200) 
cents -= toonies * 200

#loonie = 1$
loonies = int(cents / 100) 
cents -= loonies * 100

#quarter = 0.25$
quarters = int(cents/25) 
cents -= quarters * 25

#quarter = 0.10$
dimes = int(cents/10) 
cents -= dimes * 10

#nickels = 0.05$
nickels = int(cents/5)

pennies = cents

print("{} toonies, {} loonies, {} quarters, {} dimes, {} nickels, {} pennies".format\
    (toonies, loonies, quarters, dimes, nickels, pennies))

