class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = x
        r = 0
        while t > 0:
            d = t % 10
            r *= 10
            r += d
            t //= 10
        if x == r:
            return True
        return False

        