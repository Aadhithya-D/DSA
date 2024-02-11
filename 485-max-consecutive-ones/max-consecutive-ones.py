class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        t = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                t += 1
            else:
                if m < t:
                    m = t
                t = 0
        if m < t:
            m = t
        return m
        