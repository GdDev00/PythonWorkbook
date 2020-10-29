#Ex. 176

nato_phonetic_alphabet = {"A":"Alpha ","B":"Bravo ", "C":"Charlie ", "D":"Delta ", "E":"Echo ",\
    "F":"Foxtrot ", "G":"Golf ", "H":"Hotel ","I":"India ","J":"Julitet ","K":"Kilo ","L":"Lima ","M":"Mike ",\
        "N":"November ","O":"Oscar ","P":"Papa ","Q":"Quebec ","R":"Romeo ","S":"Sierra ","T":"Tango ",\
            "U":"Uniform ","V":"Victor ","W":"Whiskey ","X":"Xray ","Y":"Yankee ","Z":"Zulu "}

def spelling(word):
    #base case
    if len(word)==0:
        return ""

    #recursive case
    else:
        if word[0] in nato_phonetic_alphabet:
            return nato_phonetic_alphabet[word[0]] + spelling(word[1:])

print("Nato Phonetic Alphabet Word Converter")
word = input("Plesa insert a word to converter: ")

word = word.replace(" ","")
word = word.upper()

print(spelling(word))