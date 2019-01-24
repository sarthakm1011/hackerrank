#!/bin/python3

https://www.hackerrank.com/challenges/candies/problem

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    left = [1]*n
    right = [1]*n
    candy = []

    for i in range(n-1):
        if arr[i+1] > arr[i]:
            left[i+1] = left[i] + 1

        if arr[n-i-1-1] > arr[n-i-1]:
            right[n-i-1-1] = right[n-i-1] + 1

    for i in range(n):
        candy.append(max(left[i],right[i]))
    
    return sum(candy)


    # FAILED Solution 1
    # ----------------------
    # candy = [1]*n

    # if n == 1: return 1

    # if n == 2: 
    #     if arr[0] == arr[1]:
    #         return 2
    #     else:
    #         return 3

    # if n == 3: 
    #     if arr[1] > arr[0]:
    #         if arr[1] > arr[2]:
    #             candy[1] = max(candy[0],candy[2]) + 1
    #         if arr[1] < arr[0]:
    #             candy[1] = candy[0] + 1
    #             candy[2] = candy[1] + 1
    #         else:
    #             candy[1] = candy[0] + 1
            
    #     else:
    #         if arr[1] > arr[2]:
    #             candy[1] = candy[2] + 1
    #         else:
    #             return sum(candy)
    #     print(candy)
    #     return sum(candy)


    
    # for i in range(1,n-2):
    #     temp_1 = arr[i-1]
    #     temp_2 = arr[i]
    #     temp_3 = arr[i+1]
    #     temp_4 = arr[i+2]

    #     if arr[i] > arr[i-1]:
    #         if arr[i] > arr[i+1]:
    #             candy[i] = max(candy[i-1],candy[i+1]) + 1
    #         elif arr[i] < arr[i+1]:
    #             candy[i] = candy[i-1] + 1
    #             candy[i+1] = candy[i] + 1
    #         else:
    #             candy[i] = candy[i-1] + 1
    #     else:
    #         if arr[i] > arr[i+1]:
    #             #candy[i] += 1
    #             candy[i] = candy[i+1] + 1
    #         else:
    #             continue

    #     if i == n-3:
    #         if arr[i+1] < arr[i+2]:
    #             candy[i+2] = candy[i+1] + 1
    #         else:
    #             candy[i+1] = candy[i+2] + 1
    # print(candy)

    # return sum(candy)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
