class Solution:
    def reverse(self, x: int) -> int:
        t = abs(x)
        o = 0
        while t > 0:
            d = t % 10
            o *= 10
            o += d
            t //= 10
        if x < 0:
            o *= -1
        if o < pow(-2, 31) or o > pow(2, 31) - 1:
            o = 0 
        return o
        