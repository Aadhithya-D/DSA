class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res1 = []
        res2 = ""
        for i in s:
            if i in order:
                res1.append(i)
            else:
                res2 += i
        for i in range(len(res1) - 1):
            for j in range(0, len(res1) - i - 1):
                if order.index(res1[j]) > order.index(res1[j + 1]):
                    res1[j], res1[j + 1] = res1[j + 1], res1[j]
        res = ""
        for i in res1:
            res += i
        res += res2

        return res
