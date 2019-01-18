#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):


    cost = sorted(c, reverse=True)
    
    min_cost = 0
    
    j = 0
    for i in range(len(cost)):
        
        if (i < k):
           min_cost += cost[i]
           continue
        
        if i % k == 0:
            j += 1

        min_cost += (1+j)*cost[i]
        
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
