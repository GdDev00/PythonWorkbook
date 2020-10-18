IVA_ALIMENTARE = 10
MANCIA_PERCENTUALE = 18

costoPasto = float(input("Quant'è il costo totale del pasto senza tasse? \n"))
iva = costoPasto * IVA_ALIMENTARE /100
mancia = costoPasto * MANCIA_PERCENTUALE /100

print("Riepilogo conto:\n € %02.2f pasto \n € %02.2f iva \n € %02.2f mancia" %(costoPasto,iva,mancia))
print("Totale: € %02.2f" %(costoPasto+iva+mancia))
