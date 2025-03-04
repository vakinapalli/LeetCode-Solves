class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int sum = 0;
        int lth = nums.size() + 1;

        int a = 0;

        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            while(sum >= target){
                lth = min(lth, i - a + 1);
                sum -= nums[a];
                a++;
            }
        }
        if(lth == nums.size() + 1){ return 0;}
        return lth;
    }
};