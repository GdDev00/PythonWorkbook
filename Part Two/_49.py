magnitude = float(input("Inserisci la magnitudo: "))

if magnitude < 2.0:
	descriptor = "Micro"
elif magnitude >= 2.0 and magnitude < 3.0:
	descriptor = "Very minor"
elif magnitude >= 3.0 and magnitude < 4.0:
	descriptor = "Minor"
elif magnitude >= 4.0 and magnitude < 5.0:
	descriptor = "Light"
elif magnitude >= 5.0 and magnitude < 6.0:
	descriptor = "Moderate"
elif magnitude >= 6.0 and magnitude < 7.0:
	descriptor = "Strong"
elif magnitude >= 7.0 and magnitude < 8.0:
	descriptor = "Major"
elif magnitude >= 8.0 and magnitude < 10.0:
	descriptor = "Great"
else:
	descriptor = "Meteoric"
	
print("Questo terremoto è classificato come '{}'. ".format(descriptor))

