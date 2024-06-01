class Solution:
    def scoreOfString(self, s: str) -> int:
        o = 0
        for i in range(len(s)-1):
            t = abs(ord(s[i])-ord(s[i+1]))
            o += t
        return o