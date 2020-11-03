#Exercise 161:What’s that Element Again?
import string
import os

FILE_NAME = "elements.txt"

#load a file of chimical element into a dictionary in this way
#dict[proton] = symbol,element
#@params file_name = file to open
#@return element_dict
def load_file(file_name):
    elemet_dict = dict()
    try:
        #carico il file
        elements_file = open("elements.txt","r")
        for line in elements_file:
            line = line.rstrip()
            line = line.lower()
            
            #per ogni riga carico l'elemento in un dizionario
            #la chiave sarà il n. di protoni, il valore sarà il simbolo e l'elemento
            proton, symbol, element = line.split(",")
            elemet_dict[proton] = [symbol,element]

        return elemet_dict
    except:
        return dict()

def main():
    #load file in a dict
    element_dict = load_file(FILE_NAME)

    line = input("Please, enter a chimical element, symbol or the number of protons: ").lower()
    #if the input text is number
    if line.isdigit()==True:
        if line in element_dict:
            symbol, element = element_dict[line]
            print("The element corresponding to this number of protons is: %s (Symbol: '%s')" \
                %(element.capitalize(),symbol.capitalize()))
    else:
        for key, values in element_dict.items():
            if line in values:
                print("The number of protons for '%s' is %s" %(line.capitalize(),key))

main()