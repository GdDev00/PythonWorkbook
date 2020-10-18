#convertitore di distanza

FEET_TO_MILES = 0.000189394
FETTO_TO_YARDS = 0.333333333
FEET_FOR_INCH = 12

feet = int(input("Inserisci la distanza in piedi: "))

miles = feet * FEET_TO_MILES
yards = feet * FETTO_TO_YARDS
inches = feet * FEET_FOR_INCH

print("Miles: {}".format(miles))
print("Yards: {}".format(yards))
print("Inches: {}".format(inches))

