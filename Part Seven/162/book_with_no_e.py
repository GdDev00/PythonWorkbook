#Exercise 162: A Book with No E...

FILE =  "words.txt"

counts = {}
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    counts[ch] = 0

num_words = 0
inf = open(FILE, "r")
for word in inf:
    word = word.upper().rstrip()

    unique = []
    for ch in word:
        if ch not in unique and ch >= "A" and ch <= "Z":
            unique.append(ch)
    # Now increment the counts for all of the letters that are in the list of unique characters
    for ch in unique:
        counts[ch] = counts[ch] + 1

    num_words = num_words + 1

inf.close()

smallest_count = min(counts.values())
for ch in sorted(counts):
    if counts[ch] == smallest_count:
        smallest_letter = ch
    percentage = counts[ch] / num_words * 100
    print(ch, "occurs in %.2f percent of words" % percentage)
# Display the letter that is easiest to avoid based on the number of words in which it appears
print()
print("The letter that is easiest to avoid is", smallest_letter)