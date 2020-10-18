
def checkPassword(password):
    up_char = 0
    lower_char = 0
    number = 0
    #the password must have at least 8 characters
    if(len(password)>=8):
        for i in range(0,len(password)-1):
            if(password[i].isdigit()==True):
                number+=1
            else:
                if(password[i].isupper()==True):
                    up_char+=1
                else:
                    lower_char+=1
    else:
        return False

    if(up_char>0 and lower_char>0 and number>0):
        return True
    else:
        return False


def main():
    s = input("Inserisci la password da verificare: ")
    result = checkPassword(s)
    if (result == True):
        print("La password inserita è valida")
    else:
        print("La password inserita non è valida!")

if __name__ == "__main__":
    main()