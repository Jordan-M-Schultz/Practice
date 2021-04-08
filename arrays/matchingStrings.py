
import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
'''
Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings
Returns

int[q]: an array of results for each query
'''
def matchingStrings(strings, queries):
    if len(strings) == 0 or len(queries) == 0: 
        return -1

    s = {}
    final = []
    for a in strings:
        if a in s : 
            s[a] += 1
        else:
            s[a] = 1
    
    for b in queries:
        if b in s:
            final.append(s[b])
        else:
            final.append(0)

    return final