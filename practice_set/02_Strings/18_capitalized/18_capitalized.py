

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    #s = "hello   world"
    #s.split(' ')  ➜ ['hello', '', '', 'world']

    return ' '.join([word.capitalize() for word in s.split(' ')])   #list comprehention


if __name__ == '__main__':
    

    s = input()

    result = solve(s)

