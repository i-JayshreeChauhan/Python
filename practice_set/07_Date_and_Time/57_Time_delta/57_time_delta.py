import math
import os
import random
import re
import sys

from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    fmt = '%a %d %b %Y %H:%M:%S %z'
    #dt = datetime.strptime('Sat 02 May 2015 19:54:36 +0530', fmt)
    #print(dt)

    # Convert to datetime objects
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    # Calculate absolute time difference in seconds
    diff = abs(int((dt1 - dt2).total_seconds()))
    #print(diff)  
    return str(diff)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
