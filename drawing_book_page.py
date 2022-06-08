import math
import os
import random
import re
import sys

def pageCount(n, p):
    # Write your code here
    l=p//2
    n=n+1 if n%2==0 else n
    r=(n-p)//2
    return min(l,r)
    