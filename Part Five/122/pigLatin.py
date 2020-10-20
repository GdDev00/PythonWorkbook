#Ex. 122 Pig Latin


#Return a traslated test from English to Pig Latin
#@params text = the text to translate (all the word must be in lower case)
def convertEnglisToPigLatin(text):
    t=[]
    if(text.isalpha()==False or text.islower()==False):
        t.append("Errore, controlla che il testo inserito sia minuscolo e senza caratteri speciali!")
    
    else:
        t = text.split()
        for i in range(len(t)):
            if t[i][0]=="a" or t[i][0]=="e" or t[i][0]=="i" or t[i][0]=="o" or t[i][0]=="u":
                t[i] = t[i] + "way"
            else:
                #the first letter is a consonant
                firstVowelIndex = 0
                for c in range(len(t[i])):
                    if t[i][c] =="a" or t[i][c]=="e" or t[i][c]=="i" or t[i][c]=="o" or t[i][c]=="u":
                        firstVowelIndex=c
                        break
                
                lastWord = t[i]
                t[i] = lastWord[firstVowelIndex:]
                t[i] = t[i] + lastWord[0:firstVowelIndex] + "ay"


    return ".".join(t)

string  = input("Inserisci un testo da convertire in pig latin: ")
result = convertEnglisToPigLatin(string)
print(result)