#!/bin/python3

import math
import os
import random
import re
import sys

# Important question for performing the difference in array approach which does the updating of range of indexes in constant time complexity in a list. 

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    #arr = [0]*n
    arr = [0]*(n+1)
    for q in queries:
        start_index = q[0]
        end_index = q[1]
        value = q[2]
        
        # base = arr[start_index:end_index]
        # extra = [value]*(end_index-start_index)
        # arr[start_index:end_index] = [sum(x) for x in zip(base, extra)]

        arr[start_index-1] += value
        arr[end_index] -= value 
        #print(arr)


    for i in range(1,len(arr)):
        arr[i] += arr[i-1] # cumulative sum array
    #print(arr)
    max_value = max(arr)

    return max_value

    # store the max value and the indexes at which the max values exist, if new value greater than and changes the index s then store it's value and index. If new value smaller than max but removes all the indices of the list having max values then find the new min of the whole list using the min function.
    #indices = [i for i,x in enumerate(arr) if x == max_value]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
