from random import randint

old_plate = 1
new_plate = 2

LOW_ASCII = 65
HIGH_ASCII = 90
LOW_NUMBER_ASCII = 48
HIGH_NUMBER_ASCII = 57

def random_plate():

    count = 0    
    plate = randint(old_plate, new_plate)
    part_a = []
    part_b = []
    
    if plate == 1:
        while count <= 2:
            count += 1
            part_a.append(chr(randint(LOW_ASCII, HIGH_ASCII)))
                
    elif plate == 2:
        while count <= 3:
            count += 1
            part_a.append(chr(randint(LOW_NUMBER_ASCII, HIGH_NUMBER_ASCII)))            
            part_b.append(chr(randint(LOW_ASCII, HIGH_ASCII)))
    
    return part_a + part_b        

def main():   
    print(random_plate())
    
if __name__ == "__main__":
    main()
