class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        l = nums.copy()
        o = []
        dict1 = {}
        dict2 = {}
        for i in l:
            if i not in dict1:
                dict1[i] = 1
                dict2[i] = 0
            else:
                dict1[i] += 1
        
        while dict1 != dict2:
            t = []
            for i in l:
                if i not in t and dict2[i] < dict1[i]:
                    t.append(i)
                    dict2[i] += 1
            o.append(t)
        return o


        