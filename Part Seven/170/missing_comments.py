#Exercise 170: Missing Comments

import sys

def main():
    if len(sys.argv)==1:
        print("Missing file name in commmand line argument!")
        print("Quitting...")
        quit()

    for file_name in sys.argv[1 : len(sys.argv)]:
        try:
            inf = open(file_name,"r")
            prev = ""
            lnum = 1
            for line in inf:
                if line.startswith("def") and prev[0] != "#":
                    bracket_ind = line.find("(")
                    name = line[4:bracket_ind]
                    print("%s line %d: %s" % (file_name, lnum, name))

                prev=line
                lnum+=1
            inf.close()

        except Exception as ex:
            print("Error!")
            print(ex.args)
            print("Quitting...")
            quit()

main()