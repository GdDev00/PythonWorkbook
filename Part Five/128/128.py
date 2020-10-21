#Ex. 128 Count the elements

def countRange(t,minValue,maxValue):
    count = 0
    for element in t:
        if element>=minValue and element<maxValue:
            count+=1
    return count



t1=[1,2,3,4,5,6,7,9,10 ]
print(countRange(t1,5,8))

t2=[1.5,1.8,1.9,2.2,2.9,2.7]
print(countRange(t2,1.9,2.6))

