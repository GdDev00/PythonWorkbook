BREAD_OLD_PRIZE = 0.60
BREAD_REGULAR_PRIZE = 3.49
noOfDayOldBreadLoaves = int(input("Inserisci il numero di pagnotte di pane di ieri: "))

dayOldDiscount = BREAD_OLD_PRIZE # 60% discount

regularPrice = noOfDayOldBreadLoaves * BREAD_REGULAR_PRIZE
discountedPrice = noOfDayOldBreadLoaves * (BREAD_REGULAR_PRIZE * dayOldDiscount)

print("Prezzo normale ${:.2f}.".format(regularPrice))
print("Prezzo discount ${:.2f}.".format(discountedPrice))

