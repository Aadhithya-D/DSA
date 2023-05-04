//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
    //Function to find a continuous sub-array which adds up to a given number.
    vector<int> subarraySum(vector<int>arr, int n, long long s)
    {
          long long int tSum = 0;
        int j = 0, i = 0;
        vector<int> output;
        while (i < n && j < n){
            if (j>i){
                i=j;
                tSum = 0;
            }
            else if (arr[i] + tSum < s){
                tSum += arr[i];
                i++;
            }
            else if (arr[i] + tSum > s){
                tSum -= arr[j];
                j++;
            }
            else{
                output = {++j, ++i};
                return output;
            }
        }
        output = {-1};
        return output;
    }
};

//{ Driver Code Starts.

int main()
 {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        long long s;
        cin>>n>>s;
        vector<int>arr(n);
        // int arr[n];
        const int mx = 1e9;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        Solution ob;
        vector<int>res;
        res = ob.subarraySum(arr, n, s);
        
        for(int i = 0;i<res.size();i++)
            cout<<res[i]<<" ";
        cout<<endl;
        
    }
	return 0;
}
// } Driver Code Ends