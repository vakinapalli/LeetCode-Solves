class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int i = 0;
        int j = 0;
        int k = matrix.size()-1;
        int l = matrix[0].size()-1;
        int lengthlit = l + 1;
        int mid = 0;
        int midi = 0;
        int midj = 0;
        while(i * lengthlit + j <= k * lengthlit + l ){
            mid = ((i * lengthlit + j) + (k * lengthlit + l))/2;
            midi = mid / lengthlit;
            midj = mid % lengthlit;

            if(matrix[midi][midj] > target){
                mid--;
                k = mid / lengthlit;
                l = mid % lengthlit;
            }
            else if(matrix[midi][midj] < target){
                mid++;
                i = mid / lengthlit;
                j = mid % lengthlit;
            }
            else{
                return true;
            }

        }
        return false;
    }
};