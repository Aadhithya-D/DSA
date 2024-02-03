from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    t = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = t
    return arr
