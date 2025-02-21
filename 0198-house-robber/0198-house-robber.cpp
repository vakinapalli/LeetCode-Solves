class Solution {
public:
    int rob(vector<int>& nums) {

        for(int i = 1; i < nums.size(); i++){
            if(i == 1){
                nums[i] = max(nums[i-1], nums[i]);
            }
            else{
                nums[i] = max(nums[i-1], nums[i] + nums[i-2]);
            }
            
        }
        return nums[nums.size() - 1];
    }
};