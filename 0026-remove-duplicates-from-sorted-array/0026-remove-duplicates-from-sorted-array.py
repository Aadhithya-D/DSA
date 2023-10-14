class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = -101
                m += 1
        l = 0
        for r in range(n):
            if nums[r] != -101:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        t = n - m
        return t
        