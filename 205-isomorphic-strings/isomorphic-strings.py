class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) == len(set(t)):
            d = {i:"" for i in set(s)}
            ss = []
            for i in s:
                if i not in ss:
                    ss.append(i)
            ts = []
            for i in t:
                if i not in ts:
                    ts.append(i)
            for i in range(len(ss)):
                d[ss[i]] = ts[i]
            for i in range(len(t)):
                if t[i] != d[s[i]]:
                    return False
            return True
        return False