#CALCOLO INTERESSE

TASSO_INTERESSE = 4

totale = float(input("Saldo depositato: € "))

interesse = (totale * TASSO_INTERESSE)/100
totale += interesse
print("Saldo a fine del 1° anno: %.2f €" %totale)

interesse = (totale * TASSO_INTERESSE)/100
totale += interesse
print("Saldo a fine del 2° anno: %.2f €" %totale)

interesse = (totale * TASSO_INTERESSE)/100
totale += interesse
print("Saldo a fine del 3° anno: %.2f €" %totale)

