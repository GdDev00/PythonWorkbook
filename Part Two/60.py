import random

number = random.randint(0, 37)

if number == 0:
	if random.randint(0, 2) == 0:
		print("Paga 00")
	else:
		print("Paga 0")
		
else:
	print("The spin resulted in {}...".format(number))

	print("Pay {}".format(number))
	
	if number == 1 or number == 3 or number == 5 or number == 7 or number == 9 or number == 12 or number == 14 or number == 16 or number == 18 \
	or number == 19 or number == 21 or number == 23 or number == 25 or number == 27 or number == 30 or number == 32 or number == 34 or number == 36:
		print("Paga rosso")
	else:
		print("Paga nero")
		
	if number > 0:
		if number % 2 == 0:
			print("Paga pari")
		else:
			print("Paga dispari")
	
	if number >= 1 and number <= 18:
		print("Paga 1 -> 18")
	elif number >= 19 and number < 36:
		print("Paga 19 -> 36")
