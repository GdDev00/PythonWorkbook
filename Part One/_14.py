IN_FT = 12
CM_IN = 2.54

print("Inserisci la tua altezza: ")
feet = int(input("feet: "))
inches = int(input("in: "))

inches += feet * IN_FT

cm = inches * CM_IN

print("L'altezza in centimetri è di ", cm)
print("L'altezza in metri è di ", cm/100)


