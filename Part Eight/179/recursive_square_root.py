#Ex. 179 Recursive Square Root

def square_root(n, guess=1.0):
    if abs(guess ** 2 - n) < 10 ** (-12) * n:
        return guess
    else:
        return square_root(n, (guess+(n/guess))/2)

print("The square root of 10 is: %.3f" %square_root(10))
