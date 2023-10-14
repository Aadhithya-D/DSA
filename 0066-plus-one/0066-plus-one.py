class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = digits[0]
        for i in range(1, len(digits)):
            n *= 10
            n += digits[i]
        n += 1
        t = []
        t1 = n
        m = len(digits)
        while t1 > 0:
            t2 = t1 % 10
            t1 //= 10
            t.append(t2)
        t = t[::-1]
        return t