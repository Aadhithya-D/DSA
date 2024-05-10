class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        f = {}
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                f[arr[i]/arr[j]] = [arr[i], arr[j]]
        sorted_dict = dict(sorted(f.items()))
        m = list(sorted_dict.keys())
        m1 = m[k-1]
        return sorted_dict[m1]
