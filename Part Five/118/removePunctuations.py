#Ex. 117 Only the Words

punctuations = ",.?-_!:;"

#Remove punctuations marks at the beginning and the end of a word
#@params: s = the string to remove punctuations marks
#@return: a list of word
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
