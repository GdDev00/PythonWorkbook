frequency = float(input("Inserisci una frequenza: "))

category = ""

if frequency < 3e9:
	category = "onde radio"
elif frequency >= 3e9 and frequency < 3e12:
	category = "microonde"
elif frequency >= 3e12 and frequency < 4.3e14:
	category = "luce infrarossi"
elif frequency >= 4.3e14 and frequency < 7.5e14:
	category = "luce visibile"
elif frequency >= 7.5e14 and frequency < 3e17:
	category = "luce ultravioletta"
elif frequency >= 3e17 and frequency < 3e19:
	category = "raggi x"
elif frequency >= 3e19:
	category = "raggi gamma"
	
if category != "":
	print("Questa frequenza è nella categoria: '{}'".format(category))
else:
	print("La frequenza inserita non è valida")

