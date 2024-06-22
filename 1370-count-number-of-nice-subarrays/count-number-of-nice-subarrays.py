class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        c = [0] * (n + 1)
        c[0] = 1
        ans = 0
        t = 0
        for v in nums:
            t += v & 1
            if t - k >= 0:
                ans += c[t - k]
            c[t] += 1
        return ans
        