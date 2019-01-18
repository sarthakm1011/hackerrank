#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    s = sorted(arr)
    max_min = s[k-1]-s[0]
    for i in range(1,(len(s)-k+1)):
        if ((s[k-1+i]-s[i]) < max_min):
            max_min = s[k-1+i]-s[i]
    return max_min

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
