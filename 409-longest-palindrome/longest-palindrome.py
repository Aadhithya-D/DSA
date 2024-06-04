class Solution:
    def longestPalindrome(self, s: str) -> int:
        d =  {i:0 for i in s}
        c = 0
        for i in s:
            d[i] += 1
            if d[i] % 2 == 0:
                c += 2
        for i in d.values():
            if i%2:
                c += 1
                break
        return c