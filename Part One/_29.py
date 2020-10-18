#convertitore gradi

celsius = float(input("Inserisci la temperatura in °celsius: "))

fahrenheit = celsius * (9/5) + 32
kelvin = celsius + 273.15

print("Fahrenheit: {}".format(fahrenheit))
print("Kelvin: {}".format(kelvin))

