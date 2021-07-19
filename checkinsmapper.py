#!/usr/bin/python
import sys
import csv, os


# added to handle the error - "_csv.Error: field larger than field limit (131072)"
# csv.field_size_limit(sys.maxsize)
csv.field_size_limit(1000000)


day_values = {
            "Mon": '1',
            "Tue": '2',
            "Wed": '3',
            "Thu": '4',
            "Fri": '5',
            "Sat": '6',
            "Sun": '7'
}
line_count = 0

data = sys.stdin.readlines()

for row in csv.reader(data):
    if line_count == 0:
        pass
    else:
        
        print(row[0] + " " + day_values[row[1]]+ "\t" + row[3])

    line_count += 1