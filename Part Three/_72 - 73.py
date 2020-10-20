#VERIFICA SE UNA STRINGA E' PALINDROMA

PUNCTUATIONS = '''!()-[]{};:'",<>.?@#$%^&*_~'''

text = input("Inserisci la parola: ")


def removePunctuationMarks(text):
    string ="" 
    for char in text:
        thereIsPunctuation = False
        for mark in PUNCTUATIONS:
            if(mark==char):
                thereIsPunctuation = True

        if(thereIsPunctuation==False):
            string += char   

    return string


while (text!=""):
    i=0
    isPalindroma = True

    #NORMALIZZO LA STRINGA
    #elimino gli spazi vuoti
    text = text.replace(" ", "")
    #rendo il testo minuscolo
    text = text.lower()
    #elimino i segni di punteggiatura
    text = removePunctuationMarks(text)

    while i<=(len(text)-1):
        if(text[i] != text[len(text)-1-i]):
            isPalindroma = False  

        i+=1

    if(isPalindroma== True):
        print("La stringa è PALINDROMA")
    else:
        print("La stringa NON E' PALINDROMA")
        
    print("")
    text = input("Inserisci la parola: ")
