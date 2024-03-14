class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0: return 0

            c = 0
            l, s = 0, 0
            for r in range(len(nums)):
                s += nums[r]
                while s > x:
                    s -= nums[l]
                    l += 1
                c += (r - l + 1)
            return c
        return helper(goal) - helper(goal - 1)
            