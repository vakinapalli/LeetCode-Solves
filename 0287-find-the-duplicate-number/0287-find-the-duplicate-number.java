class Solution {
    public int findDuplicate(int[] nums) {
        for(int i = 0; i < nums.length; i++){
            nums[nums[i] % nums.length] += nums.length;
            
        }
        for(int i = 0; i < nums.length; i++){
            if( nums[i] > nums.length * 2){
                return i;
            }
        }
        return 0;

    }
}