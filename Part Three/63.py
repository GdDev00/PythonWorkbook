#show temperature conversion table (°C->°F)

for i in range(0,101,10):
    kelvin = i+273.15
    fahrenheitTemp = ((kelvin - 273.15) * 1.8)+32 

    print("%.2f °C --> %.2f °F" %(i,fahrenheitTemp))