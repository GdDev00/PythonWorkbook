#Exercise 164: Gender Neutral Names

#check neutral names in the entered year
#@params year -> year where find the name
#@return a list contain all neutral names
def check_neutral_names(year):
    boys_file_name = "BabyNames\\"+str(year) + "_BoysNames.txt"
    girls_file_name = "BabyNames\\"+str(year) + "_GirlsNames.txt"

    boys_file = open(boys_file_name,"r")
    girls_file = open(girls_file_name, "r")

    boys_names = []
    girls_names = []
    neutral_names = []
    #load all boys names in that year
    for line in boys_file:
        line = line.rstrip()
        boys_names.append(line.split()[0])

    #load all girls names in that year
    for line in girls_file:
        line = line.rstrip()
        girls_names.append(line.split()[0])

    for name in boys_names:
        if name in girls_names:
            if name not in neutral_names:
                neutral_names.append(name)

    boys_file.close()
    girls_file.close()
    
    return neutral_names

def main():
    print("Get the neutral name in years from 1900 to 2012!")

    year = input("Please, enter the years (1900-2012): ")
    if year.isdigit():
        while(int(year)<1900 or int(year)>2012):
            print("The inserted value is incorrect!")
            year = input("Please, enter the years (1900-2012): ")
    else:
        print("You must enter a number!")
        print("Quitting...")

    #check netrual names and store it in alist
    neutral_names = check_neutral_names(year)

    #print result
    if len(neutral_names)==0:
        print("In that year there aren't neutral names!")
    else:
        print("Here the neutral names for %s:" %year)
        for name in neutral_names:
            print("- %s" %name)
main()