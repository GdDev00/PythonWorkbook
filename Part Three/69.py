pi = 3

for i in range(1,16):
    if(i==1):
        pi += 4/((i*1)*(i*2)*(i*3))
    else:
        temp = i*2
        pi -= 4/((temp)*(temp+1)*(temp+2))

    print("Approssimazione PI {0} = {1}".format(i, pi))

 