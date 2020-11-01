#Ex. 186

def compress(data):
    #base case
    if len(data)==0:
        return []

    index = 1
    while index < len(data) and data[index] == data[index-1]:
        index += 1
        
    compressed = [data[0], index]

    return compressed + compress(data[index : len(data)])

def main():
    # Read a string from the user
    s = input("Enter some characters: ")

    # Display the result
    print("When those characters are run-length encoded," "the result is:", compress(s))
    
main()    

