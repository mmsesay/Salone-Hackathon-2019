#!/usr/bin/python3

# dictionary
greetings = {"key": "value", "ab": "hi there", "we": "say what"}

for k,v in greetings.items():
    """ Loop through every item in the dictionary and print"""
    print((k ,':', v))