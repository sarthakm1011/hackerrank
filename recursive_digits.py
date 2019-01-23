#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):

    # Base Case
    if len(n) == 1:
        return n 

    v = sum(int(x) for x in n) # converting string to int important
    v = v*k # just a multiple of the calculated number
    v = str(v) # Input is a string for the function

    return superDigit(v,1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
