#Exercise 160:Weird Words
import os
import string

follow_rule = []
unfollow_rule = []

#check if a word follow the rule of 'I before E except after C'
#@params w -> the word to analyse
#@return True if the word follow the rule
#@return False if the word unfollow the rule
def word_follow_rule(w):
    if w.find("cei") != -1:
        return True
        #follow rule

    elif w.find("cie") != -1:
         #unfollow the rule
        return False

    elif w.find("ie") != -1:
            #followe rule
            return True
    
    else:
        #unfollow the rule
        return False

def main():
    file_name = input("Please, enter the file name to analyze:")
    #check if the file exists
    while os.path.isfile(file_name) == False:
        print("File name isn't valid!")
        file_name = input("Please, enter the file name to open: ")

    try:
        inf = open(file_name,"r")
        for line in inf:
            line = line.rstrip()
            for word in line.split():
                word = word.lower()
                word = word.strip(string.punctuation)
                
                #if the word contain an adjacent E and I or I and E
                if word.find("ei") != -1 or word.find("ie") != -1:
                    #cehck if the word follow the rule
                    if word_follow_rule(word):
                        #add the word to follow rule list
                        follow_rule.append(word)
                    else:
                        #add the word to unfollow rule list
                        unfollow_rule.append(word)

        #print result
        if len(follow_rule)>0:
            print("There are %d word that follow the rule of 'I before E except after C':")
            for word in follow_rule:
                print(word)

        if len(unfollow_rule)>0:
            print("There are %d word that unfollow the rule of 'I before E except after C':")
            for word in unfollow_rule:
                print(word)


    except Exception as e:
        print("Error: %s"%e.args)

main()