class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        o = [[0 for i in range(n-2)] for j in range(n-2)]
        def findMax(i1, j1):
            m = 0

            for i in range(i1-1, i1+2):
                for j in range(j1-1, j1+2):
                    m = max(m, grid[i][j])
            return m
        for i in range(n-2):
            for j in range(n-2):
                o[i][j] = findMax(i+1, j+1)
        return o
