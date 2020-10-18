TEASPOONS_TO_TBLSPOONS = 3
TEASPOONS_FOR_CUP = 48

def reduceMeasure(num, unit):
    unit = unit.lower()
    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * TEASPOONS_TO_TBLSPOONS
    elif unit == "cup" or unit == "cups":
        teaspoons = num * TEASPOONS_FOR_CUP

    cups = teaspoons // TEASPOONS_FOR_CUP
    teaspoons = teaspoons - cups * TEASPOONS_FOR_CUP
    tablespoons = teaspoons // TEASPOONS_TO_TBLSPOONS
    teaspoons = teaspoons - tablespoons * TEASPOONS_TO_TBLSPOONS

    result = ""

    if cups > 0:
        result = result + str(cups) + " cup"

        if cups > 1:
            result = result + "s"

    if tablespoons > 0:

        if result != "":
            result = result + ", "

        result = result + str(tablespoons) + " tablespoon"

        if tablespoons > 1:
            result = result + "s"

    if teaspoons > 0:
        if result != "":
            result = result + ", "
        result = result + str(teaspoons) + " teaspoon"

        if teaspoons > 1:
            result = result + "s"

    if result == "":
        result = "0 teaspoons"

    return result