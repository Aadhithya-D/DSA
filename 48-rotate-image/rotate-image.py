class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in matrix:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        n = len(temp)
        for i in range(n):
            t = []
            for j in range(n-1,-1,-1):
                t.append(temp[j][i])
            for j in range(n):
                matrix[i][j] = t[j]
        return matrix