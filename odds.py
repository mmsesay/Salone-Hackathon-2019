#!/usr/bin/pyhthon

# list of numbers initialization
numbers = [1, 2, 3, 4, 5, 7]

# odd number function
def find_odd_number(num):
    """ This function return all odd number """
    return num%2 != 0

if __name__=="__main__":
    # using the filter function to pass every number as the parameter in the
    # find_odd_number then cast them back to a list
    print(list(filter(find_odd_number,numbers)))
