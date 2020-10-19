#Ex. 117 Only the Words

punctuations = ",.?-_!:;"


def onlyWords(s):
    t = s.split()
    returnList=[]
    for word in t:
        for char in punctuations:
            if (word[0]) == char:
                word = word[1:]
            if (word[-1]) == char:
                word = word[:(len(word)-1)]
        returnList.append(word)

    return returnList

line = input("Inserisci una stringa: ")
s = onlyWords(line)
for word in s:
    print(word)

