#!/usr/bin/python

# function declaration
def longestWordCheck():
    """ This function returns the longest word in the list of string.
    If their is a match length of words, all matches will be return. """ 

    # list of words definition
    wordPack = ["hello", "world", "hi", "bye"]

    # mapping every word in the list to the length function and returning
    #  the max of them
    maxWord = max(map(len,wordPack))

    # looping through the words
    for word in wordPack:
        # checking if the length of each word matches the maxmimum word above
        if len(word) == maxWord :
            print(word)  # print the word(s)

if __name__=="__main__":
    # strating the longestWordCheck function here
    longestWordCheck()
    