#User function Template for python3
import math

class Solution:
    def digitsInFactorial(self,N):
        # code here
        n = 0.0
        for i in range(1, N+1):
            n += math.log10(i)
        n = math.floor(n) + 1
        return n

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input("Num:"))
        ob=Solution()
        print(ob.digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends