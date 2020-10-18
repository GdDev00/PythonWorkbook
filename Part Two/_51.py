A_PLUS = 4.0
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0


grade = input("Inserisci il voto : ")

points = -1

if grade == "A+":
	points = A_PLUS
elif grade == "A":
	points = A
elif grade == "A-":
	points = A_MINUS
elif grade == "B+":
	points = B_PLUS
elif grade == "B":
	points = B
elif grade == "B-":
	points = B_MINUS
elif grade == "C+":
	points = C_PLUS
elif grade == "C":
	points = C
elif grade == "C-":
	points = C_MINUS
elif grade == "D+":
	points = D_PLUS
elif grade == "D":
	points = D
elif grade == "F":
	points = F
	
if points >= 0:
	print(points)
else:
	print("La votazione inserita non è valida!")
