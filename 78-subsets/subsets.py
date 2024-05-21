import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for num in nums:
            powersetCopy = copy.deepcopy(powerset)
            powersetCopy.pop(-1)
            for s in powerset:
                s.append(num)
            powerset.extend(powersetCopy)
            powerset.append([])
        return powerset