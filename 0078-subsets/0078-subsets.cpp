class Solution {
public:

    void backtrack(vector<int>& nums, vector<vector<int>>& ans, vector<int> hold, int it){
        ans.push_back(hold);

        for(int i = it; i < nums.size(); i++){
            hold.push_back(nums[i]);
            backtrack(nums, ans, hold, i+1);
            hold.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> hold;
        backtrack(nums, ans, hold, 0);
        return ans;
    }
};