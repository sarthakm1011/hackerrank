#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the triplets function below.
def triplets(a, b, c):
    a, c = sorted(set(a)), sorted(set(c))
    return sum([bisect.bisect(a, x)*bisect.bisect(c, x) for x in set(b)])
    # bisect resturn the position at whhich new element should be added to maintain the sorting order of the solution.

    # Brute Force Solution (Same thing is done below in easy looking way)
    #--------------------
    # a = list(sorted(set(a)))
    # b = list(sorted(set(b)))
    # c = list(sorted(set(c)))
    
    # ai = 0
    # bi = 0
    # ci = 0
    
    # ans = 0
    
    # while bi < len(b):
    #     while ai < len(a) and a[ai] <= b[bi]:
    #         ai += 1
        
    #     while ci < len(c) and c[ci] <= b[bi]:
    #         ci += 1
        
    #     ans += ai * ci
    #     bi += 1
    
    # return ans


    # Failed Solution 1
    # --------------------
    # new_b = sorted(b)
    # max_b = max(new_b)

    # a.sort()
    # new_a = a
    # for i in range(len(a)):
    #     if max_b < a[i]:
    #         new_a = a[:i+1]

    # c.sort()
    # new_c = c
    # for i in range(len(c)):
    #     if max_b < c[i]:
    #         print(i)
    #         new_c = c[:i+1]

    # new_a = list(set(new_a))
    # new_b = list(set(new_b))
    # new_c = list(set(new_c))
    # count = len(a)*len(b)*len(c) 
    
                    
    # return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
