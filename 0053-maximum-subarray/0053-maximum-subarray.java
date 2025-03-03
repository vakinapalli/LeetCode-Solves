class Solution {
    public int maxSubArray(int[] nums) {
        int maxi = nums[0];
        int cur = 0;

        for(int i = 0; i < nums.length; i++){
            cur = Math.max(0,cur);
            cur += nums[i];
            maxi = Math.max(maxi,cur);
        }
        return maxi;
    }
}