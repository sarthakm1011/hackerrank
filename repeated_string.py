# https://www.hackerrank.com/challenges/repeated-string/submissions/code/54689587?
#h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import sys
import math

s = input().strip()
n = int(input().strip())

count = 0    

for i in range(0,len(s)):
    if (s[i:i+1] == 'a'):
        count += 1

multiply_by = math.floor(n / len(s))
remainder_string = n % len(s)

count *= multiply_by

for i in range(0,remainder_string):
    if(s[i:i+1] == 'a'):
        count += 1

print(count)        
