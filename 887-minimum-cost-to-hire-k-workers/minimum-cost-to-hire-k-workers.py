class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        r = float("inf")
        pairs = []
        for i in range(len(quality)):
            pairs.append((wage[i]/quality[i], quality[i]))
        pairs.sort(key = lambda p:p[0])
        
        maxHeap = []
        t = 0
        for rate, q in pairs:
            heapq.heappush(maxHeap, -q)
            t += q

            if len(maxHeap) > k:
                t += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                r = min(r, t*rate)
        return r