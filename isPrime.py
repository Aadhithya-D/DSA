import math
class Solution:
    def isPrime(self, N):
        if N <= 1:
            return False
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return False
        return True


#{ 
 # Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        
        ob=Solution()
        if(ob.isPrime(N)):
            print("Yes")
        else:
            print("No")
        T-=1
    
    
if __name__=="__main__":
    main()
# } Driver Code Ends