#Exercise 156: Sum a Collection of Numbers

number_sum = 0

line = input("Please, input a valid number: ")
while line != "":
    try:
        number_sum+=float(line)
        print("The sum is %d"%number_sum)

    except:
        print("You must enter a valide number!")

    line = input("Please, input a valid number: ")
