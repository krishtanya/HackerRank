#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact



if __name__ == '__main__':
#   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)
    print(result)

#    fptr.write(str(result) + '\n')

#    fptr.close()
