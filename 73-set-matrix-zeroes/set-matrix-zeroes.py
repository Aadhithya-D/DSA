class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    z.append([i, j])
        for k in z:
            for i in range(len(matrix[0])):
                matrix[k[0]][i] = 0
            for i in range(len(matrix)):
                matrix[i][k[1]] = 0