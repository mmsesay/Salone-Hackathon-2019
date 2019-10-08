#!/usr/bin/python

def readTxtFile():
    """ This function opens and reads the txt file """ 
    # opening the file
    with open('helloworld.txt', mode='r') as txtFile:
        """ Read from the file line by line and closes automatically
        after printing the #10 line. """

        count = 0  # will hold the iteration count

        # looping through the file line by line
        for f in txtFile.readlines():
            count += 1   # incrementing the count

            # equality check for desired line
            if count == 10:
                print('the 10TH line is-> ', f)  # outputting the #10 line

if __name__=="__main__":
    # strating the readTextFile function
    readTxtFile()
