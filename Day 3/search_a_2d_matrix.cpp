class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        vector<int> l1;
        for (int i = 0; i < matrix.size(); i++){
            l1.insert(l1.end(), matrix[i].begin(), matrix[i].end());
        }
        int l = 0;
        int r = l1.size() - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
    
            // Check if x is present at mid
            if (l1[m] == target)
                return true;
    
            // If x greater, ignore left half
            if (l1[m] < target)
                l = m + 1;
    
            // If x is smaller, ignore right half
            else
                r = m - 1;
        }
        return false;
    }
};