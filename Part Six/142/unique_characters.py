#Ex. 142

char_frequency = dict()

line = input("Inserisci una stringa: ")

for char in line:
    char_frequency[char] = True

print("La frase ha %d caratteri unici" %len(char_frequency))
