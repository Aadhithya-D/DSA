class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = 0
        for i in nums:
            if i > 0:
                if i > m:
                    if (-1*i) in nums:
                        m = i
        return -1 if m == 0 else m