class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        t = []
        for i in score:
            t.append(i)
        t.sort(reverse=True)
        d = {}
        m = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in score:
            ind = t.index(i)
            if ind < 3:
                d[i] = m[ind]
            else:
                d[i] = str(ind+1)
        return list(d.values())