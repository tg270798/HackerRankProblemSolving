#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(aliceList, bobList):
    # Write your code here
    retList = []
    ap = 0
    bp = 0
    for (a,b) in zip(aliceList,bobList):
        if(a>b):
            ap +=1
        elif(a<b):
            bp +=1
        else:
            ap+= 0
            bp+= 0
    
    retList.append(ap)
    retList.append(bp)
    return retList
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    aliceList = list(map(int, input().rstrip().split()))

    bobList = list(map(int, input().rstrip().split()))

    result = compareTriplets(aliceList, bobList)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
