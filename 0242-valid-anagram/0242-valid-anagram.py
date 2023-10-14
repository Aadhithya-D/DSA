class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0] * (26)
        k = [0] * (26)
        for i in s:
            l[ord(i)-97] += 1
        for i in t:
            k[ord(i)-97] += 1
        if l == k:
            return True
        return False

        