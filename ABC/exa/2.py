#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getSubstringCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getSubstringCount(s):
    count = 0
    prev_len, now_len = 0, 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            now_len += 1
        else:
            count += min(prev_len, now_len)
            prev_len = now_len
            now_len = 1
    
    count += min(prev_len, now_len)
    return count

if __name__ == '__main__':

    s = input()

    result = getSubstringCount(s)
    print(result)
