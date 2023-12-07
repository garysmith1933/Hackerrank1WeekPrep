#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    pm_times = {}
    s = s.split(":")
    hour, minutes, seconds, time_of_day = s[0], s[1], s[2][0:2], s[2][2:]
    
    if hour == '12':
        if time_of_day == 'PM':
            return ':'.join([hour, minutes, seconds])
        
        else:
            return ':'.join(["00", minutes, seconds])
            
    elif time_of_day == 'AM':
        return ':'.join([hour, minutes, seconds])
      
    else:
        old_hour = 1
        new_hour = 13
        
        while old_hour != 12:
            pm_times[str(old_hour)] = str(new_hour)
            old_hour += 1
            new_hour += 1
        
        converted_hour = pm_times[str(int(hour))]
        return ':'.join([converted_hour, minutes, seconds])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
