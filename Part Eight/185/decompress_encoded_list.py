#Ex. 185 Decompresses a run-length encoded list

#Compressionis achieved by replacing groups of
# repeated values with one copy of the value, 
# followed by the number of times that it should be repeated
#

def decompress(enc_list):
    if len(enc_list)==0:
        return []

    else:
        decompressed = []

        #if the 
        if enc_list[1]>0:
            decompressed.append(enc_list[0])
            enc_list[1] = enc_list[1]-1
            return decompressed + decompress(enc_list)
        else:
            return decompressed + decompress(enc_list[2:])


        

test = ["A", 6, "B", 5, "C", 10]
print(decompress(test))