#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    i,sumTotal =0,0
    for a in range(len(arr)):
        sumTotal+= arr[a]
        maxVal,minVal = 0,9999999999999
        
    while (i<5):
        sumT = sumTotal
        
        sumT = sumT - arr[i]
        if(sumT>maxVal):
            maxVal = sumT
        if(sumT<minVal):
            minVal = sumT
        
        i+=1
    print(minVal,maxVal)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
