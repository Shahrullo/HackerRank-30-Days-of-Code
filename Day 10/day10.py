import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = list(bin(n)[2:])
    
    c = 0
    max_c = 0
    for i in binary:
        if (i == '1'):
            c += 1
        else:
            if c > max_c:
                max_c = c
            c = 0
    if c > max_c:
        max_c = c
    print(max_c)