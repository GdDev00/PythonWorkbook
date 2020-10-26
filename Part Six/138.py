#Ex. 138 Text Messaging

key_simbols = {"1":['.',',','?','!',':'],"2":['A','B','C'],"3":['D','E','F'],\
    "4":['G','H','I'],"5":['J','K','L'], "6":['M','N','O'], "7":['P','Q','R','S'],\
        "8":['T','U','V'],"9":['W','X','Y','Z'], "0": " "}
list_key = key_simbols.keys()

words = input("Inserisci una frase da convertire: ")
words= words.upper()
for char in words:
    for i in list_key:
        if char in key_simbols[i]:
            print(i* (key_simbols[i].index(char)+1))