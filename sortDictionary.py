#!/usr/bin/python

def sortDictionary():
    """ This function sort the dictionary based on keys. """

    # dictionary inistialization
    greetings = {"key": "value", "ab": "hi there", "we": "say what"}

    # sorting the dictionary by keys and casting it back to dictionary
    print(dict(sorted(greetings.items())))

if __name__=="__main__":
    # strating the sortDictionary function here
    sortDictionary()