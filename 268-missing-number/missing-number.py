class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(1)
        for i in range(len(nums)-1):
            if nums[i] != -1*(len(nums)):
                if nums[abs(nums[i])]:
                    nums[abs(nums[i])] = -1*abs(nums[abs(nums[i])])
                else:
                    
                    nums[abs(nums[i])] = -1*(len(nums))
            else:
                nums[0] = -1*abs(nums[0])
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i
        return -1
            