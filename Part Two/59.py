

licensePlate = input("Inserisci targa: ")

if licensePlate[0].isalpha() and licensePlate[1].isalpha() and licensePlate[2].isalpha():
    if licensePlate[0].isupper() and licensePlate[1].isupper() and licensePlate[2].isupper():
        if licensePlate[3].isdecimal() and licensePlate[4].isdecimal() and licensePlate[5].isdecimal():
            if len(licensePlate) == 6:
                print("Formato vecchia targa")
            else:
                print("Targa non valida!")
        else:
            print("Targa non valida!")
    else:
        print("Targa non valida!")
else:
    if licensePlate[0].isdecimal() and licensePlate[1].isdecimal() and licensePlate[2].isdecimal() and licensePlate[3].isdecimal():
        if licensePlate[4].isalpha() and licensePlate[5].isalpha() and licensePlate[6].isalpha():
            if licensePlate[4].isupper() and licensePlate[5].isupper() and licensePlate[6].isupper():
                if len(licensePlate) == 7:
                    print("Formato nuova targa")
                else:
                    print("Targa non valida!")
            else:
                print("Targa non valida!")
        else:
            print("Targa non valida!")
    else:
        print("Targa non valida!")        
        
            
            
