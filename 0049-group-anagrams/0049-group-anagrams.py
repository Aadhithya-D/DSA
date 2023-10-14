class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            t = [0]*26
            for j in i:
                t[ord(j)-97]+=1
            t = tuple(t)
            if t in d:
                d[t].append(i)
            else:
                d[t] = [i]
        out = d.values()
        return out