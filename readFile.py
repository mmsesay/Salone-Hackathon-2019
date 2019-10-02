#!/usr/bin/ python3

# opening the file
with open('helloworld.txt', mode='r') as file:
    """ Read from the file line by line and closes automatically
    after printing the #10 line. """

    count = 0  # will hold the iteration count

    for f in file.readlines():
        # looping through the lines

        count += 1   # incrementing the count

        # equality check for desired line
        if count == 10:
            print(f)  # outputting the #10 line
