def convertStringNumber(numberInteger):
    if numberInteger == 1:
        return "one"
    if numberInteger == 2:
        return "two"
    if numberInteger == 3:
        return "three"
    if numberInteger == 4:
        return "four"
    if numberInteger == 5:
        return "five"
    if numberInteger == 6:
        return "six"
    if numberInteger == 7:
        return "seven"
    if numberInteger == 8:
        return "height"
    if numberInteger == 9:
        return "nine"
    if numberInteger == 10:
        return "ten"
    if numberInteger == 11:
        return "eleven"
    if numberInteger == 12:
        return "twelve"
    else:
        return ""


def main():
    for i in range(1,13):
        print(convertStringNumber(i))

if __name__ == "__main__":
    main()