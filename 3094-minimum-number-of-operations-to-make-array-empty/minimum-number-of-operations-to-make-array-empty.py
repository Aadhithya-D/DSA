class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        o = 0
        for i in dict1:
            if dict1[i] >= 3:
                if dict1[i] % 3 == 0:
                    o += 0
                elif dict1[i] % 3 == 1:
                    dict1[i] -= 4
                    o += 2
                elif dict1[i] % 3 == 2:
                    dict1[i] -= 2
                    o += 1
                o += dict1[i]//3
                dict1[i] -= dict1[i]
            elif dict1[i] == 2:
                o += 1
                dict1[i] -= dict1[i]
            elif dict1[i] == 1:
                return -1
        return o

        