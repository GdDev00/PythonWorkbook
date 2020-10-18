#convertitore pressione

kiloPascals = float(input("Inserisci la pressione in kilo-pascals: "))

PSI = kiloPascals * 0.145037738
mmOfMercury = kiloPascals * 7.50062
atmospheres = kiloPascals / 101.3

print("Risultati: ")
print("(PSI): {}".format(PSI))
print("(mmHg): {}".format(mmOfMercury))
print("(atm): {}".format(atmospheres))

