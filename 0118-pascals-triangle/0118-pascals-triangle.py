class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        output = []
        output.append([1])
        if (n == 2):
          output.append([1, 1])
        elif n > 2:
          output.append([1, 1])
          print(output)
          for i in range(2, n):
            t = [[] for _ in range(0, i+1)]
            t[0] = 1
            t[-1] = 1
            for j in range(1, i):
              t[j] = output[i-1][j-1] + output[i-1][j]
            output.append(t)
        
        return output


