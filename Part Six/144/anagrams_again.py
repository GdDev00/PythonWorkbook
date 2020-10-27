#Ex. 144 Anangrams Again

puntuaction_marks = ["?","!",".",",",":","'",'"'," "]

def count_char(words):
    chars_dict = dict()

    text = words.lower()
    for char in text:
        if char not in puntuaction_marks:
            if char in chars_dict:
                chars_dict[char]+=1
            else:
                chars_dict[char]=1
                
    return chars_dict


string1 = input("Inserisci una frase: ")
string2 = input("Inserisci la frase da confrontare: ")

counts1 = count_char(string1)
counts2 = count_char(string2)

if counts1 == counts2:
    print("Le frasi inserite sono anagrammi!")
else:
    print("Le frasi inserite non sono anagrammi!")

