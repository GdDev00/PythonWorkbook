#Ex. 121 Generate Lottery Number

import random


#Generate x numbers from range
#@params extrationMinNumber -> minimum number to extract
#@params extrationMaxNumber -> maximum number to extract
#@params numberToGenerate -> the number of extracts to be generate
def generateLotteryNumber(extrationMinNumber, extrationMaxNumber, numberToGenerate):
    numbers = []

    for i in range(0,numberToGenerate):
        num  = random.randint(extrationMinNumber,extrationMaxNumber)
        while num in numbers:
            num  = random.randint(extrationMinNumber,extrationMaxNumber)

        numbers.append(num)
    return numbers


def main():
    line = input("Premi invio per generare i numeri della lotteria")

    print("Ecco i 6 numeri: ")
    print(generateLotteryNumber(1,49,6))

main()