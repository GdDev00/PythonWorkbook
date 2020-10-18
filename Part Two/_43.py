sommaBanconote = int(input("Inserisci la banconota: $"))

nome = ""

if sommaBanconote == 1:
	nome = "George Washington"
if sommaBanconote == 2:
	nome = "Thomas Jefferson"
if sommaBanconote == 5:
	nome = "Abraham Lincoln"
if sommaBanconote == 10:
	nome = "Alexander Hamilton"
if sommaBanconote == 20:
	nome = "Andrew Jackson"
if sommaBanconote == 50:
	nome = "Ulysses S. Grant"
if sommaBanconote == 100:
	nome = "Benjamin Franklin"
	
if nome == "":
	print("Non esiste una banconota americana in circolazione!")
else:
	print(nome)


