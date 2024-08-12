import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    #most_common() is used to produce a sequence of the n most frequently encountered input values and their respective counts
    result=Counter(sorted(s)).most_common(3)
    print(s)
    print(result)

    for key, val in result:
        #print(key)
        #print(val)
        print(key,val)
