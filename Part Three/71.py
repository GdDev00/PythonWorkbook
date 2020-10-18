def validateGuess(guess,x):
    if(guess * guess - x <= 10e-12):
        return True
    else:
        return False 

x = float(input("Inserisci un numero intero: "))

guess = x/2

while validateGuess(guess,x)==False:
    guess = (guess + (x/guess)) /2

print(guess)