#Exercise 165: Most Births in a given Time Period

NAME_DATASET_FOLDER = "BabyNames"

#return the most popoular name in that selected years (yearStart, yearEnd)
#@return a tuple with the most popoular boyName, girlName
def check_most_popoular_names(yearStart, yearEnd):
    boys_popoular_names = dict()
    girls_popoular_names = dict()
    year = int(yearStart)

    while year<=int(yearEnd):
        boys_file_name = "BabyNames\\"+ str(year) + "_BoysNames.txt"
        girls_file_name = "BabyNames\\"+ str(year) + "_GirlsNames.txt"

        boys_file = open(boys_file_name,"r")
        girls_file = open(girls_file_name, "r")

        for line in boys_file:
            line = line.rstrip()
            name, frequency = line.split()
            boys_popoular_names[name]= frequency

        for line in girls_file:
            line = line.rstrip()
            name, frequency = line.split()
            girls_popoular_names[name]= frequency
        
        boys_file.close()
        girls_file.close()
        year+=1


    max_value = max(boys_popoular_names.values())
    boys_most_popoular_name = ""
    girls_most_popoular_name = ""

    for key, value in boys_popoular_names.items():
        if value==max_value:
            boys_most_popoular_name = key

    max_value = max(girls_popoular_names.values())
    for key, value in girls_popoular_names.items():
        if value==max_value:
            girls_most_popoular_name = key

    return (boys_most_popoular_name,girls_most_popoular_name)


def main():
    year1 = input("Please, enter the begin year (1900-2012): ")
    if year1.isdigit():
        while(int(year1)<1900 or int(year1)>2012):
            print("The inserted value is incorrect!")
            year1 = input("Please, enter the years (1900-2012): ")
    else:
        print("You must enter a number!")
        print("Quitting...")

    
    year2 = input("Please, enter the end year (1900-2012): ")
    if year2.isdigit():
        while(int(year2)<1900 or int(year2)>2012):
            print("The inserted value is incorrect!")
            year2 = input("Please, enter the years (1900-2012): ")
    else:
        print("You must enter a number!")
        print("Quitting...")

    if year1 > year2:
        print("Value not valid!")
        print("Quitting...")
        quit()
        
    boy, girl = check_most_popoular_names(year1,year2)
    print("The most popoular boy name in that year is '%s'" %boy)
    print("The most popoular girl name in that year is '%s'" %girl)

main()