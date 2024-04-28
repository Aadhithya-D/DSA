class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = str(bin(start))
        g = str(bin(goal))
        c = 0
        s = s.replace("0b", "")
        g = g.replace("0b", "")
        if len(s) > len(g):
            t = "0"*(len(s)-len(g))
            g = t+g
        elif len(g) > len(s):
            t = "0"*(len(g)-len(s))
            s = t+s
        for i in range(len(s)):
            if s[i] != g[i]:
                c += 1
        return c