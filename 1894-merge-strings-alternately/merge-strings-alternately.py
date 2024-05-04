class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        o = ""
        for i in range(n):
            o+=word1[i]
            o+=word2[i]
        if len(word1) > len(word2):
            t = word1[n:]
            o+=t
        elif len(word2) > len(word1):
            t = word2[n:]
            o+=t
        return o
        