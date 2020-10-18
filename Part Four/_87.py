###
#CENTER A STRING OF CHARACTERS
###



#CREATE A NEW STRING THAT WILL BE CENTERED WITHIN A GIVEN WIDTH WHEN IT IS PRINTED
# @params s is the string that will be centered
# @params width is the widht in which the string will be centered
# @return is the return of formatted string
def centraStringa(s, widht):
    if(len(s) > widht):
        return s

    spaces = ((widht-len(s))//2)
    newS = " "*spaces + s
    return newS


def main():
    line=input("Inserisci stringa: ")
    print(centraStringa(line, 80))

main()