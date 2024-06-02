import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        min_heap = []
        d = {}            
        for i in range(len(s)):                
            if s[i] != '*':
                heapq.heappush(min_heap, s[i])
                if s[i] not in d:
                    d[s[i]] = [i]
                else:
                    d[s[i]].append(i)
            else:
                while min_heap:
                    smallest_char = heapq.heappop(min_heap)
                    d[smallest_char].pop()
                    # s = s[:i] + s[i+1:]
                    break
        l = []
        for i in list(d.values()):
            l += i
        l.sort()
        result = ""
        for i in l:
            result += s[i]
        return result

        