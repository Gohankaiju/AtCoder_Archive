#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING input_str as parameter.
#

def getString(input_str):
    last_found = {}
    for i, char in enumerate(input_str):
        last_found[char] = i
    
    result = []
    seen = set()
    for i, char in enumerate(input_str):
        if char in seen:
            continue
        
        while result and result[-1] < char and last_found[result[-1]] > i:
            seen.remove(result.pop())
        result.append(char)
        seen.add(char)
    ans = ''.join(result)
    return ans
    

    
if __name__ == '__main__':
    
    input_str = input()

    result = getString(input_str)
    print(result)

