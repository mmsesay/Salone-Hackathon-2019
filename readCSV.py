#!/usr/bin/python
import csv

def readCSVFile():
    """ This function reads a CSV file, finds matching keys and sum up the values """

    # opening the csv file
    with open('helloworld.csv', mode='r') as csvFile:
        """ Read from the file line by line and closes automatically. """

        # reading from the csv file and saving the content to the contents variable
        contents = csv.reader(csvFile)

        finalDict = {}  # will hold the final dictionary

        # looping through the content
        for row in contents:

            stripComma = ', '.join(row)  # removing square brakets [] from the rows
            fullString = stripComma.replace(',', '')  # replacing the comma's with a space
            
            fullStringWords = fullString[:12]  # slicing all 11 characters from the string
            fullStringValues = fullString[-1]  # slicing only the values from the string
            
            newWords = [fullStringWords]   # converting the fullStringWords to a list
            values = [int(fullStringValues)]  # converting the fullStringValues to a list of integers

            # Zipping line 22 and 23 variables.
            # Then cast it to a list and then cast it to a dictionary
            newDict = dict(list(zip(newWords, values)))

            # looping through the new dictionary 
            for key,val in newDict.items():

                # check if the key not existing in the finalDict
                # Then add it 
                if key not in finalDict.keys():
                    finalDict[key] = key  # adding the a new key
                    finalDict[key] = val  # adding the a value
                else: 
                    finalDict[key] += val  # summing up the values of new key to the existing key 

        print(finalDict)  # outputting the final dictionary

if __name__=="__main__":
    # strating the readCSVFile function
    readCSVFile()
