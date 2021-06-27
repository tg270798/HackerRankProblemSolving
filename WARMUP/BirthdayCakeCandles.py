#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    N = len(candles)
    count = 0
    lis = []
    '''for i in range(0,N-1):
        for j in range(0,N-i-1):
            if(candles[j]>candles[j+1]):
                candles[j],candles[j+1] = candles[j+1],candles[j]
    tried using bubble sort but it failed some testcases 
    so better use python's builtin sorting technique which uses timsort technique
    '''
    
    lis = sorted(candles)
   #print(candles)
    maxV = lis[N-1]
    for a in candles:
        if(a==maxV):
            count+=1
    
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
