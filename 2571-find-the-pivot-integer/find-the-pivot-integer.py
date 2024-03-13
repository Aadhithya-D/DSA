class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        for i in range(1, n+1):
            t1 = (i*(i+1))/2
            t = i+1
            t2 = ((n*(n+1))/2) - ((t*(t+1))/2)
            print(t1, t2)
            if t1 == t2:
                return i+1
        return -1