class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {i:0 for i in range(1, len(nums)+1)}
        du = 0
        for i in nums:
            d[i] += 1
            if d[i] > 1:
                du = i
        m = 0
        for i in d:
            if d[i] == 0:
                m = i
        return [du, m]
            

        