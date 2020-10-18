def triangle(a, b, c):

    if a >= b + c:
        triangle = False
    elif b >= a + c:
        triangle = False
    elif c >= b + a:
        triangle = False        
    else:
        triangle = True
    
    if triangle == False:
        return False
    elif triangle == True:
        return True
        

def main():
    a = float(input("Inserisci lato A: "))
    b = float(input("Inserisci lato b B: "))
    c = float(input("Inserisci lato  C: "))
    
    if(triangle(a, b, c) == True):
        print("è un triangolo!")
    else:
        print("non è un triangolo!")

if __name__ == "__main__":
    main()
    
