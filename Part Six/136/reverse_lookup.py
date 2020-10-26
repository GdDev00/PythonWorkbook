#Ex. 136 Reverse Lookup


#Finds all of the keys in a dictionary that map to a specific value
#@params dictionary -> the dictionary where find the value
#@params value -> the value to find
#@return -> a list of all keys found
def reverse_lookup(dictionary, value):
    keys = []
    for k in dictionary:
        if dictionary[k]==value:
            keys.append(k)
    return keys

def main():
    dictionary = dict()
    dictionary = {"a":"1","b":"6","c":"6", "d":"8"}

    print(dictionary)
    print("I will found '6' value: ")
    result = reverse_lookup(dictionary, "6")
    print("'6' is contained in keys: ")
    for k in result:
        print(k)

main()
