#calcola le radici reali di un'equazione quadratica (se presente)
a = float(input("Inserisci un valore per a: "))
b = float(input("Inserisci un valore per b: "))
c = float(input("Inserisci un valore per c: "))

discriminate = b**2 - 4*a*c

if discriminate < 0:
	print("Questa funzione quadratica non ha radici reali.")
	
elif discriminate == 0:
	print("Questa funzione quadratica ha una vera radice.")
	
	root = -b / 2*a 
	
	print("Radice reale: {}".format(root))
	
elif discriminate > 0:
	print("Questa funzione quadratica ha due radici reali.")
	
	root1 = -b + discriminate / 2*a
	root2 = -b - discriminate / 2*a 
	
	print("Radice reale: {} o {}".format(root1, root2))

