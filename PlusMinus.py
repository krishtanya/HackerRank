#!/bin/python3
'''
#import math
#import os
#import random
#import re
#import sys
'''
# Complete the plusMinus function below.
def plusMinus(arr):

    positive = 0
    negative = 0
    zero = 0
    
    for i in arr:
        if i > 0:
            positive +=1
        elif i < 0:
            negative +=1
        else:
            zero +=1
        
    print("{:.5f}".format(positive/n))
    print("{:.5f}".format(negative/n))
    print("{:.5f}".format(zero/n))

 #   except:
 #       raise KeyError("Invalid Input")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
