
line = int(input("Inserisci un intero (0 per uscire): "))
s=[]


while line!=0:
    s.append(line)
    line = int(input("Inserisci un intero (0 per uscire): "))

s.sort(reverse=True)
print(s)

