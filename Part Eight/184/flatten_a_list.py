#Ex. 184 -- Flatten a list

def flatten_list(data):
    if len(data)==0:
        return []

    if type(data[0]) is list:
        l1 = flatten_list(data[0])
        l2 = flatten_list(data[1:])
        return l1 + l2
    
    if type(data[0]) is not list:
        l1 = [data[0]]
        l2 = flatten_list(data[1:])
        return l1 + l2


#Test the function
test1 = [1, [2, 3], [4, [5, [6, 7]]],[[[8], 9], [10]]]
test2 = [[1,[3,1],5,4] [2, 8], [4, [5, [6, 7]]],[[[8], 9], [10]]]
print(flatten_list(test1))
print(flatten_list(test2))