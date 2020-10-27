#Ex. 143 Anagrams

def char_count(word):
    chars_dict = dict()

    for char in word:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    
    return chars_dict

    
word1 = input("Inserisci una parola: ").lower()
word2 = input("Insersci la parola da confrontare: ").lower()

counts1 = char_count(word1)
counts2 = char_count(word2)

if counts1 == counts2:
    print("Le parole sono anagrammi!")
else:
    print("Le parole non sono anagrammi!")