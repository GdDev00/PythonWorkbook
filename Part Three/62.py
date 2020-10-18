NUMBER_OF_PRICE = 5

for item in range(NUMBER_OF_PRICE):
	orignalPrice = NUMBER_OF_PRICE*item + 4.95
	discountedPrice = (orignalPrice *60) /100
	
	print("Prezzo originale: $%.2f | Prezzo scontato: $%.2f " %(orignalPrice,discountedPrice))