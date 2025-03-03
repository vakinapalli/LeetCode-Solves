class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int maxi = nums[0];
        int mini = nums[0];
        int curmax = 0;
        int curmin = 0;
        int sum = 0;
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            curmax = max(curmax, 0);
            curmin = min(curmin, 0);
            curmax += nums[i];
            curmin += nums[i];
            maxi = max(maxi, curmax);
            mini = min(mini, curmin);
        }
        if(sum == mini){
            return maxi;
        }
        return max(maxi, sum - mini);
    }
};