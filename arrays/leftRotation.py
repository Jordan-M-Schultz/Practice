#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    if len(arr) == 0 or d % len(arr) == 0: # no shift at all
        return arr
    
    rot = d - len(arr) if d > len(arr) else d
    return arr[rot:len(arr)] + arr[:rot]


print(rotateLeft(7 , [1,2,3,4]))
print(rotateLeft(1 , [1,2,3,4]))
print(rotateLeft(2 , [1,2,3,4]))
print(rotateLeft(3 , [1,2,3,4]))

