class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                t = prices[r] - prices[l]
                if t > maxPro:
                    maxPro = t
                r += 1
        return maxPro