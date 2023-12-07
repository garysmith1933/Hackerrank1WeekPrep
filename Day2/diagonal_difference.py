#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



def diagonalDifference(arr):
    
    def isValidPosition(pos):
        return pos >= 0 and pos <= len(arr) - 1
    
    l_row, l_col = 0, 0
    left_to_right = 0
    
    while isValidPosition(l_row) and isValidPosition(l_col):
        left_to_right += arr[l_row][l_col]
        l_row += 1
        l_col += 1
    
    r_row, r_col = 0, len(arr) - 1
    right_to_left = 0
    
    while isValidPosition(r_row) and isValidPosition(r_col):
        right_to_left += arr[r_row][r_col]
        r_row += 1
        r_col -= 1
    
    return abs(left_to_right - right_to_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
