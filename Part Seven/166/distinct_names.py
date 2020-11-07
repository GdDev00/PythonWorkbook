#Exercise 166: Distinct Names
import os

def main():
    boys_names = dict()
    girls_names = dict()
    directory = os.getcwd()+"\\BabyNames\\"
    for file_name in (os.listdir(directory)):
        inf = open(directory+file_name,"r")
        for line in inf:
            line = line.rstrip()
            if file_name.find("Boys") != -1:
                boys_names[line.split()[0]] = 0
            elif file_name.find("Girls") != -1:
                girls_names[line.split()[0]] = 0

        inf.close()

    print("Boys names: ")
    for name in boys_names:
        print(name)
    print("--- --- ---")

    print("")
    print("")
    print("")


    print("Girl names:")
    for name in girls_names:
        print(name)
    print("--- --- ---")

main()