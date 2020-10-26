#Ex. 139 Morse Code

morse_dictionary = {"A":".-","B":"-...","C":"-.-.", "D":"-..", "E":".", "F": "..-.",\
    "G":"- -.", "H": "....", "I":"..", "J":".- - -", "K":"-.-", "L":".-..","M":"- -",\
        "N":"-.","O":"---", "P":".- -.", "Q":"- -.-","R":".-.", "S":"...", "T":"-", \
            "U":"..-","V":"...-","W":".- -","X":"-..- ","Y":"-.- -", "Z":"- -..",\
                "0":"-----", "1":".- - - -", "2":"..- - -", "3":"...- -", "4":"....-",\
                    "5":".....","6":"-....","7":"- -...","8":"- - -..","9":"- - - -."}

words = input("Inserisci la parola da convertire in codice morse: ")
words = words.upper()
dict_keys = morse_dictionary.keys()

for char in words:
    for key in dict_keys:
        if key == char:
            print (morse_dictionary[key])

