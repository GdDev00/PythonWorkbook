#Ex. 145 Scrabble Score

scrabble_score = {1:["A","E","I","L","N","O","R","S","T","U"],\
    2:["D","G"],3:["B","C","M","P"], 4:["F","H","V","W","Y"],\
        5:"K",8:["J","X"],10:["Q","Z"]}

def calculate_score(word):
    result = 0
    for char in word:
        for key,value in scrabble_score.items():
            if char in value:
                result+= key
    return result


word = input("Inserisci una parola: ").upper()
result = calculate_score(word)
print("Il punteggio è %d" %result)
