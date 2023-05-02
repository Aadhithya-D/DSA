#User function Template for python3

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        #Your code here
        #No need to print the array
        zero = 0
        for i in A:
            if i == 0:
                zero+=1
        
        one = N-zero
        
        for i in range(zero):
            A[i] = 0
        
        for i in range(zero, N):
            A[i] = 1
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            N=int(input())
            A=list(map(int,input().split()))
            obj = Solution()
            obj.binSort(A,N)
            
            for i in A:
                print(i,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends