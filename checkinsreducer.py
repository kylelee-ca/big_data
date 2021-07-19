#!/usr/bin/python
import sys


previous = None
sum = 0 
day_values = {
    '1': "Mon",
    '2': "Tue",
    '3': "Wed",
    '4': "Thu",
    '5': "Fri",
    '6': "Sat",
    '7': "Sun"
}

for line in sys.stdin:
    key, checkins = line.split("\t")
    id, day = key.split()
    if [id, day] != previous:
        if previous != None:    
 
            print(previous[0] + ", " + day_values[previous[1]] + ", " + str(sum))
        previous = [id, day]
        sum = 0
    sum += int(checkins)

print(previous[0] + "\t" + day_values[previous[1]] + "\t" + str(sum))