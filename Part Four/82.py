BASE_TAXI_FARE = 4.00
EXTRA_TAXI_FARE = 0.25


def calculateTaxiFares(km):
    total = BASE_TAXI_FARE
    m = km * 1000
    total += (m/140)*EXTRA_TAXI_FARE
    return total

def main():
    km = float(input("Inserisci i km percorsi: "))
    taxes = calculateTaxiFares(km)
    print("La tariffa da pagare è di $ %.2f" %taxes)

main()