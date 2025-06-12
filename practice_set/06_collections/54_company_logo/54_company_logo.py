

import math
import os
import random
import re
import sys

from collections import OrderedDict

d = OrderedDict()
init_count = 1

if __name__ == '__main__':
    s = input()

    for i in s:
        if i not in d:
            d[i] = init_count
        else:
            d[i] += 1


    # Sort by values in descending order
    #sorted_desc = OrderedDict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_desc)

    #pick first 3 values 
    #upd_dict =  OrderedDict( list(sorted_desc.items())[:3] )
    #print(upd_dict)
        
    sorted_items = sorted(d.items(), key=lambda item: (-item[1], item[0]))
    sorted_od = OrderedDict(sorted_items)

    #pick first 3 values 
    upd_dict =  OrderedDict( list(sorted_od.items())[:3] )
    #print(upd_dict)

    for key, value in upd_dict.items():
        print(f"{key} {value}")