#Ex. 141 Write out Numbers in English

#dictionary for number between 1 and 9
dict1= {"1":"one", "2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

#dictionary for number between 10 and 19
dict2 = {"10":"ten","11":"eleven","12":"twelve", "13":"thirteen", "14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen",\
    "19":"nineteen"}

#dictionary for multiples of 10
dict3 = {"2":"twenty","3":"thirty","4":"fourty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninety"}

def number_in_english(number):
    result = ""
    lenght = len(number)


    while lenght>0:
        if lenght==1:
            if number[0] in dict1:
                result += dict1[number[0]] + " "           
            number = number[1:]

        elif lenght==2:
            if int(number)<20:
                if number in dict2.keys():
                    result += dict2[number] + " "
            else:
                if number[0] in dict3.keys():
                    result += dict3[number[0]] + " "
            number = number[1:]

        elif lenght==3:
            result += dict1[number[0]] + " hundred "
            number = number[1:]

        else:
            print("Numero inserito non valido!")

        lenght = len(number)

    return result


number= input("Inserisci un numero: ")
result = number_in_english(number)
print(result)