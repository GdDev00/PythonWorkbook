#Ex. 179 Recursive Square Root

def square_root(n, guess=1.0):
    print(n*(10**-12))
    if guess**2 < n*(10**-2):
        return guess
    else:
        return square_root(n, (guess+(n/guess))/2)

print(square_root(10))