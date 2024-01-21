from typing import List
import math

def printDivisors(n: int) -> List[int]:
    # Write your code here
    l = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            l.append(i)
            if i != n//i:
                l.append(n//i)
    l.sort()
    return l
