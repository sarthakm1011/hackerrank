#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    
    gg = sorted(contests, key = lambda x: x[0], reverse=True)
    #contests = gg

    L = []
    T = []
    luck = 0

    for c in gg:
        L.append(c[0])
        T.append(c[1])

    
    # To maximise the luck 
    lost_important = 0
    for i in range(len(T)):

        if lost_important >= k:
            if T[i] == 1:
                luck -= L[i]
                continue

        if T[i] == 1:
            lost_important += 1
        
        luck += L[i]

    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
