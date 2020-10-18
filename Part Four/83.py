ONE_ITEM_SHIPPING_COST  = 10.95
OTHER_ITEM_SHIPPING_COST = 2.95

def calculateShippingCost(nOfItems):
    if(nOfItems==1 and nOfItems>0):
        return ONE_ITEM_SHIPPING_COST
    else:
        return ONE_ITEM_SHIPPING_COST + OTHER_ITEM_SHIPPING_COST*(nOfItems-1)

def main():
    cost = calculateShippingCost(int(input("Inserisci il numero degli articoli: ")))
    print("Il costo delle spese di spedizione è di $ %.2f" %cost)

main()