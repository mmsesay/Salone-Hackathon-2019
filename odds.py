#!/usr/bin/ pyhthon3

# list of numbers
numbers = [1, 2, 3, 4, 5, 7]

# odd number function
def find_odd_number(num):
    """ This function return a odd number """
    return num%2 != 0

# using the filter function 
print(list(filter(find_odd_number,numbers)))