#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    dict = {}
    maxi = 0
    for i in range(len(arr)):
        n = arr.count(arr[i])
        if n > maxi:
            maxi = n 
        dict[arr[i]] = n
    mini = 10000000
    for i in dict:
        if dict[i] == maxi and i < mini:
            mini = i
    return mini

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
