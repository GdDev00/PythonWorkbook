#Exercise 180: String Edit Distance

def calculate_edit_distance(s,t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1
    d1 = calculate_edit_distance(s[0 : len(s) - 1], t) + 1
    d2 = calculate_edit_distance(s, t[0 : len(t) - 1]) + 1
    d3 = calculate_edit_distance(s[0 : len(s) - 1] , t[0 : len(t) - 1]) + cost

    return min(d1, d2, d3)

def main():
    print("Compute the edit distance between two strings!")
    s1 = input("Please, insert the first string-> \n")
    s2 = input("Please, insert the second string-> \n")

    print("")
    print("The edit distance between %s and %s is %d" %(s1,s2,calculate_edit_distance(s1,s2)))

main()