R = 8.314


P = float(input("Pressione in Pascal: "))
V = float(input("Volume in litri: "))
T = float(input("Temperatura in Kelvin: "))

n = (P*V) / (R*T)

print("Quantità di gas: {}.".format(n))

