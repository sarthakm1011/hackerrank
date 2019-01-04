#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    
    for i, v in enumerate(q):
        if (v-1-i > 2):
            print("Too chaotic")
            return

        for j in range(max(v-1-1,0),i-1+1):

            # Check numbers ahead(less in index)
            # from actual pos of number to current position check which numbers are larger than the number
            if q[j] > v-1:
                swaps += 1

    ## Does not run because of bad time complexity.     
    # for i in range(last_index):
    #     for j in range(last_index):
    #         if (q[j] > q[j+1]):
    #             q[j], q[j+1] = q[j+1], q[j] # Interesting & Important
    #             swaps += 1
    
    print(swaps)
    return 

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
