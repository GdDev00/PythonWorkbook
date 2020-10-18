PESO_WIDGET = 75
PESO_GIZMO = 12

nWidgets = int(input("Inserisci numero Widgets: "))
nGizmo = int(input("Inserisci numero Gizmo: "))

pesoTotale = nWidgets * PESO_WIDGET + nGizmo * PESO_GIZMO 
print("")
if pesoTotale <1000:
    print("Il peso totale dell'ordine è di: %i g " %(pesoTotale))
else:
    pesoTotKg = pesoTotale / 1000.0
    print("Il peso totale dell'ordine è di: %.2f Kg" %(pesoTotKg))

input("")