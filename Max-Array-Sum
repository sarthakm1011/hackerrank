#Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    
    incl = 0
    excl = 0
    for i in range(0,len(arr)):
        temp = incl;
        incl = max(arr[i]+excl, temp);
        excl = temp;

    return max(incl, excl);
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    
    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


