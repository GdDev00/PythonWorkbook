# Ex. 123 Pig Latin Improved
import string  

#Return a traslated test from English to Pig Latin
#@params text = the text to translate 
def convertEnglisToPigLatin(text):
    t=[]

    #convert text to list
    t = text.split()

    for i in range(len(t)):
            firstLetterIsUpper = t[i][0].isupper()

            t[i] = t[i].lower()

            #if the first char is a vowel
            if t[i][0]=="a" or t[i][0]=="e" or t[i][0]=="i" or t[i][0]=="o" or t[i][0]=="u":
                t[i] = t[i] + "way"
                if firstLetterIsUpper:
                    t[i] = t[i].capitalize()

            #if the first letter is a consonant
            else:
                #find the first vowel and save the index in a variable
                firstVowelIndex = 0
                for c in range(len(t[i])):
                    if t[i][c] =="a" or t[i][c]=="e" or t[i][c]=="i" or t[i][c]=="o" or t[i][c]=="u":
                        firstVowelIndex=c
                        break                                
                #copy the original word
                lastWord = t[i]
                #delete the characters up to the first vowel
                t[i] = lastWord[firstVowelIndex:]
                #set the end of word + "ay"
                t[i] = t[i] + lastWord[0:firstVowelIndex] + "ay"

                if firstLetterIsUpper:
                    t[i] = t[i].capitalize()

            #check if there is a punctuations
            oldPunctuations = []
            for char in t[i]:
                if char in string.punctuation:
                    oldPunctuations.append(char)
                    t[i] = t[i].replace(oldPunctuations[-1], "")

            if len(oldPunctuations)>0:
                for char in oldPunctuations:
                    t[i] = t[i]+char
            

    return ".".join(t)

line = input("Inserisci il testo da convertire: ")
print(convertEnglisToPigLatin(line))