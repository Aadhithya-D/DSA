#User function Template for python3
# Problem Link: https://www.geeksforgeeks.org/batch/dsa-python-self-paced/track/list-advanced-python/problem/longest-subarray-of-evens-and-odds
class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        
        #returns: the maximum length
        
        #code here
        flag = arr[0]%2 == 0 
        m = 0
        t = 1
        for i in range(1, n):
            if (arr[i]%2 != 0) and flag:
                t += 1
                flag = False
            elif (arr[i]%2 == 0) and not flag:
                t += 1
                flag = True
            elif (arr[i]%2 == 0) and flag:
                if t > m:
                    m = t
                t = 1
            elif (arr[i]%2 != 0) and not flag:
                if t > m:
                    m = t
                t = 1
        if t > m:
            m = t
        return m
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maxEvenOdd(arr,n))
# } Driver Code Ends
