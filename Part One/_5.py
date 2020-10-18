#DEPOSITO DI BOTTIGLIE


menoDiUnLitro = int(input("Quante bottiglie hai da meno di un litro? "))
piuDiUnLitro = int(input("Quante bottiglie hai da più di un litro? "))

refund = menoDiUnLitro * 0.10 + piuDiUnLitro * 0.25

print("Il tuo rimborso sarà di € %.2f" %(refund))