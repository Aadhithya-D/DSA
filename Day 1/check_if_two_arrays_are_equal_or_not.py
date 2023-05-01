#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        dict = {}
        for i in A:
            if i not in dict:
                dict[i] = 0
        
        for i in A:
            dict[i]+=1;
        for i in B:
            if i in dict:
                dict[i]-=1
            else:
                return False
        
        n = len(dict)
        t = 0
        for i in dict:
            if dict[i] == 0:
                t+=1
        
        if t == n:
            return True
        
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends