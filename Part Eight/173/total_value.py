#Ex. 173 Total the Value

def total():
    val = input("Inserisci un valore: ")

    #Base case
    if val == "":
        return 0
    else:
        return float(val)+total()

def main():
    result = total()
    print("The sum is: %d" %result)

main()