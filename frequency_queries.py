#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

# Complete the freqQuery function below.
def freqQuery(queries):
    # Counter: dictionary, if key not exist then value = 0
    freq = Counter() 
    count = Counter() 
    result = []
    for q in queries:
        #print(count) # dictionary of count of frequencies
        #print(freq) # dictionary with frequency of each item 
        if q[0] == 1: # insert x
            count[freq[q[1]]] -= 1
            # if freq exists in count then remove this value of freq in count and update it to a new value after the updation of freq. For example a new number comes then the value is decreased and increased to a same value, otherwise it increases to create a new entry if it does not exist or increase an existing value.
            freq[q[1]] += 1 # insertion
            count[freq[q[1]]] += 1
        
        elif q[0] == 2: # del x
            if freq[q[1]] > 0:
                count[freq[q[1]]] -= 1
                freq[q[1]] -= 1 # deletion
                count[freq[q[1]]] += 1
        
        else: # count freq z
            if count[q[1]] > 0:
                result.append(1)
            else:
                result.append(0)
    return result


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

    ##### The right solution but with bad time complexity
    # def insert_x(x):
    #     freq_list.append(x)
    #     return 
    
    # def delete_y(y):
    #     if y in freq_list:
    #         freq_list.remove(y)
    #     return 

    # def frequency_z(z):
    #     counts = dict()
    #     flag = 0
        
    #     for i in freq_list:      
    #         counts[i] = counts.get(i,0) + 1
        
    #     for k,v in counts.items():
    #         if v == z:
    #             flag = 1
    #             return flag
    #     flag = 0
    #     return flag

        
    # freq_list = []
    # ans = []
    # for q in queries:    
    #     if q[0] == 1:
    #         insert_x(q[1]) # insert x
    #         continue
        
    #     if (q[0] == 2 and len(freq_list) > 0):
    #         delete_y(q[1]) # Delete y in the list
    #         continue

    #     if (q[0] == 3):
    #         a = frequency_z(q[1]) # check occurance of any integer = z
    #         ans.append(a)


    # return ans
