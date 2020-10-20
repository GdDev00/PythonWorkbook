#Ex. 118 Word by Word Palindromes

#Import solution from ex. 117 for export a list from a string
from removePunctuations import onlyWords

def checkIsPalindrome(text):
    t = onlyWords(text)

    isPalindrome = True
    for i in range (0,len(t)):
        if t[i].lower() != t[len(t)-i-1].lower():
            isPalindrome = False
            break
    
    return isPalindrome
    

s = input("Inserisci una stringa: ")

if(checkIsPalindrome(s)==True):
    print("La stringa è PALINDROMA!")
else:
    print("La stringa inserita NON E' PALINDROMA!")

