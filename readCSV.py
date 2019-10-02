#!/usr/bin/ python3
import csv

# opening the file
with open('helloWorld.txt', mode='r') as file:
    """ Read from the file line by line and closes automatically. """

    csv_reader = csv.DictReader(file)

    line_count = 0
    for row in csv_reader:
        # if line_count == 0:
        line_count += 1

        ask = {}

        print(f'Column names are {", ".join(row)}')
            
       
    print(f'Processed {line_count} lines.')
