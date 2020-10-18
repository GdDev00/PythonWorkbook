#calculate admission price of a group in a zoo

totalPrice = 0.0

line = input("Inserisci l'età del visitatore: ")
while line != "":
    eta = float(line)
    if(eta <2):
        eta = eta
    elif (eta>=3 and eta<=12):
        totalPrice+=14
    elif (eta>=13 and eta <=64):
        totalPrice += 23
    elif(eta>=65):
        totalPrice += 18

    line = input("Inserisci l'età del visitatore: ")

print("Il gruppo dovrà pagare $: %.2f" %totalPrice)