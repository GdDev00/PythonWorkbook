#79
import random

MIN_NUMBER = 1
MAX_NUMBER = 100

max_value = random.randint(1,100)
update=0
c=0
while c<100:
    num = random.randint(1,100)
    print(num, end="  ")
    if(num>max_value):
        max_value=num
        update +=1
        print("<--- UPDATE MAX VALUE")
    else:
        print("")
    c=c+1

print("IL NUMERO MASSIMO E' %.d" %max_value)
print("IL NUMERO TOTALE DI AGGIORNAMENTI è DI %.d" %update)