class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used =  []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        # consider: 1.path 2.options, 3.ending condition
        # ending
        if len(self.track) == len(nums):
            self.res.append(self.track.copy())
            return
        for i in range(len(nums)):
            if self.used[i]:
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.backtracking(nums)
            # post order
            self.used[i] = False
            self.track.pop()
        