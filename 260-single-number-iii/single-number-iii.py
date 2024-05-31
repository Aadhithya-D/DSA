class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        a = 0
        b = 0
        diff_bit  = 1
        while not (diff_bit & xor):
            diff_bit = diff_bit << 1
        for i in nums:
            if i & diff_bit:
                a ^= i
            else:
                b ^= i
        return a, b