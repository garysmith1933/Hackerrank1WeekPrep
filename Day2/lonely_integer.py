#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # initalize hashmap
    # iterate over list, add counts as values, nums as keys
    # iterate over hashmap, key with value of 1, all others would have 2
    # return that value
    
    counts = {}
    
    for num in a:
        counts[num] = counts.get(num, 0) + 1
    
    for num, count in counts.items():
        if count == 1:
            return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
