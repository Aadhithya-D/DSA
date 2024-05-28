class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        c = []
        for i in range(len(s)):
            t1 = abs(ord(s[i])-ord(t[i]))
            c.append(t1)
        print(c)
        cC = 0
        o = 0
        l = 0
        for r in range(len(s)):
            cC += c[r]
            while cC > maxCost:
                cC -= c[l]
                l += 1
            o = max(o, r-l+1)
        return o