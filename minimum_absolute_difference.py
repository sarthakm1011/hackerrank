#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    
    arr2 = list(set(arr))
    arr2.sort()
    print(arr2)

    if len(arr) == 1: 
        return arr[0]

    if len(arr2) == 1:
        return 0

    if len(arr2) < len(arr):
        return 0
       
    min_value = arr2[1]-arr2[0]
    for i in range(len(arr2) - 1):
        if ((arr2[i+1] - arr2[i]) < min_value):
            min_value = arr2[i+1] - arr2[i]
    
    return min_value
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
