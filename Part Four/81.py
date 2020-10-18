import math

def calculateHypotenuse (lenghtSideA, lenghtSideB):
   return math.sqrt((lenghtSideA**2)+(lenghtSideB**2))
 

def main():
    sideA = float(input("Inserisci lunghezza lato A: "))
    sideB = float(input("Inserisci lunghezza lato B: "))
    hypotenuse  = calculateHypotenuse(sideA, sideB)
    print("L'ipotenusa è: %.4f " %hypotenuse)

main()