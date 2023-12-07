#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    res = [0] * len(arr)
    prefix, postfix = 0, 0
    
    for i in range(len(arr)):
        res[i] += prefix
        prefix += arr[i]
        
    for i in range(len(arr)-1, -1, -1):
        res[i] += postfix
        postfix += arr[i]
    

    minNum = min(res)
    maxNum = max(res)
    print(minNum, maxNum)
  

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
