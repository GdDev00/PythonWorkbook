def capitalize(strings):
    result = strings.replace(" i ", " I ")
    
    if len(strings) > 0:
        result = result[0].upper() + \
        result[1 : len(result)]
        
    pos = 0
    
    while pos < len(strings):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            pos = pos + 1
            
            while pos < len(strings) and result[pos] == " ":
                pos = pos + 1
                
            if pos < len(strings):
                result = result[0 : pos] + \
                result[pos].upper() + \
                result[pos + 1 : len(result)]
            
        pos = pos + 1
        
    return result

def main():
    strings = input("Inserisci una stringa: ")
    capitalized = capitalize(strings)
    print(capitalized)

main()
