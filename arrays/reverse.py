import math
import os
import random
import re
import sys

def reverseArray(a):
    if len(a) == 1:
        return a[0]
    
    reverse = []
    for i in range(len(a) -1, -1, -1):
        reverse.append(a[i])
    return reverse


ar = [4,3,2,1]

print(reverseArray(ar))