class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s = "abcdefghijklmnopqrstuvwxyz"
        d1 = {i:{j:0 for j in s} for i in words}
        words = set(words)
        for i in words:
            for j in i:
                d1[i][j] += 1
        o = []
        for i in s:
            t = float("inf")
            for j in words:
                t = min(t, d1[j][i])
            t1 = [i for j in range(t)]
            o += t1
        return o