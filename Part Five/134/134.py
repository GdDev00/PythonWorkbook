#Ex. 134 Generate All Sublists of a List
from listSubstring import isSublist

def everySublistOfList(data):
    sublists = [[]]

    for length in range(1, len(data) + 1):
        for i in range(0, len(data) - length + 1):
            sublists.append(data[i : i + length])

    return sublists

def main():
    print("The sublists of [1, 2] are: ")
    print(everySublistOfList([1, 2]))
    print("The sublists of [1, 2, 3] are: ")
    print(everySublistOfList([1, 2, 3]))
    print("The sublists of [1, 2, 3, 4] are: ")
    print(everySublistOfList([1, 2, 3, 4]))

main()