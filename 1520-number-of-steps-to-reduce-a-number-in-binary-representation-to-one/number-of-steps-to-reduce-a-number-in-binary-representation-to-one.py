class Solution:
    def numSteps(self, s: str) -> int:
        n = 0
        for i in s:
            n = n*2 + int(i)
        c = 0
        t = n
        while t > 1:
            if t % 2 == 0:
                t = t//2
            else:
                t += 1
            c += 1
        return c