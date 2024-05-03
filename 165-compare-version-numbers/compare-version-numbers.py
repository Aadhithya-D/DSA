class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        if len(v1) < len(v2):
            t = [0 for i in range(len(v2)-len(v1))]
            v1 += t
        elif len(v1) > len(v2):
            t = [0 for i in range(len(v1)-len(v2))]
            v2 += t
        print(v1, v2)
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
        