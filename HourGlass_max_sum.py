#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(a):
    n=len(a)
    max=-99999
    count=0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if (a[i][j]+a[i-1][j]+a[i+1][j]+a[i-1][j-1]+a[i+1][j+1]+a[i+1][j-1]+a[i-1][j+1])>max:
                max=a[i][j]+a[i-1][j]+a[i+1][j]+a[i-1][j-1]+a[i+1][j+1]+a[i+1][j-1]+a[i-1][j+1]
            count+=1;    
    print(count)
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
