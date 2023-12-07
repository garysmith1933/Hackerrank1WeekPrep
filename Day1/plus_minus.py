#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        
        elif num < 0:
            neg += 1
        
        else:
            zero += 1
    
    pos_ratio = pos / len(arr)
    neg_ratio = neg / len(arr)
    zero_ratio = zero / len(arr)
    print(f'{pos_ratio:.6f}')
    print(f'{neg_ratio:.6f}')
    print(f'{zero_ratio:.6f}')
  

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)