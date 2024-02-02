class Solution:
    def check(self, nums: List[int]) -> bool:
        # m = float('-inf')
        # for i in nums:
        #     if i > m:
        #         m = i
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         if i+2<=len(nums)-1:
        #             if nums[i] != m or nums[i+1] > nums[i+2]: 
        #                     return False
        # return True
        op = 0
        l = len(nums)
        for i in range(l):
            if nums[(i+1)%l] >= nums[i]: 
                pass
            else:
                op += 1
                if op > 1:
                    return False
        else:
            return True
        