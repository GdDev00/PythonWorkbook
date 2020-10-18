#tabelline

x=0
y=1

#stampo la prima riga
print("    ", end="")
for i in range(1,10+1):
        print('\033[1m'+'{:>4}'.format(i),end="")

print("")
while(y<=10):
    x=1
    print('{:>4}'.format((y)),end="")
    while(x<=10):
        print('{:>4}'.format((x*y)),end="")
        x+=1
    print("")
    y+=1

