#User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        # code here
        sum = int(((n+1)/2)*(arr[0]+arr[-1]))
        t = 0
        for i in arr:
            t+=i
        t = sum - t
        return t


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMissing(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends