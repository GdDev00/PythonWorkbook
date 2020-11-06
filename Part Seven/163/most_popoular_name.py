#Exercise 163: Names that Reached Number One

import os

NAME_DATASET_FOLDER = "BabyNames"

#return the most popoular name
#@parmas gendre -> 'B' for boys, 'G' for girls
#@params years -> an year between 1900 to 2012
def check_most_popoular_names(gendre, years):
    if gendre == "B": #Boys
        path = "BabyNames\\"+str(years) + "_BoysNames.txt"
    elif gendre == "G":
        path ="BabyNames\\"+str(years) + "_GirlsNames.txt"
    else:
        return ""

    inf = open(path,"r")
    line = inf.readline()
    line = line.rstrip()
    name = line.split()[0]
    inf.close()
    return name


def main():
    print("Get the most popoular name in years from 1900 to 2012!")

    print("Please, enter gender: ")
    gendre = input("Enter 'B' for Boys, 'G' for Girls: ").upper()
    if gendre=="G" or gendre=="B":
        year = input("Please, enter the years (1900-2012): ")
        if year.isdigit():
            while(int(year)<1900 or int(year)>2012):
                print("The inserted value is incorrect!")
                year = input("Please, enter the years (1900-2012): ")
        else:
            print("You must enter a number!")
            print("Quitting...")
        name = check_most_popoular_names(gendre,year)
        if name!="":
            #print result
            if gendre == "G":
                print("The most popoular girl name in %s is: %s " %(year, name) )
            elif gendre == "B":
                print("The most popoular boy name in %s is: %s " %(year, name) )
        else:
            print("Value not valid!")

    else:
        print("The inserted value is incorrect!")
        quit()
    

main()