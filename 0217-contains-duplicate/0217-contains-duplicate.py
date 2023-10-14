class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = 0
        for i in nums:
            if d[i] == 0:
                d[i]+=1
            else:
                return True                
        return False
        