#Ex. 124 Line of Best Fit

x=[]
y=[]

line = input("Inserisci coordinata X: ")
while line != "":
    x.append(float(line))
    
    line = input("Inserisci coordinata Y: ")
    if line !="":
        y.append(float(line))

    line = input("Inserisci coordinata X: ")


m = 0
n = len(x)
averageX = sum(x)/n
averageY = sum(y)/n

numerator = 0
denominator = 0
for i in range(n):
    numerator += (x[i] - averageX) * (y[i] - averageY)
    denominator += (x[i] - averageX)**2

m = numerator/denominator
 
b = averageY - (m * averageX)

print("y = %.3f + %.3f" %(m,b))
    
