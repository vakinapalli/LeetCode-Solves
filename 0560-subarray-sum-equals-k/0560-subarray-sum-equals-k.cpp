class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int,int> prefixes;
        prefixes[0] = 1;
        int ct = 0;
        int cursum = 0;
        for(int i = 0; i < nums.size(); i++){
            cursum += nums[i];
            int dif = cursum - k;
            ct += prefixes[dif];
            prefixes[cursum]++;
        }
        return ct;
    }
};