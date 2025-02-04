/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let freq = Array(3).fill(0);
    for(let i = 0; i < nums.length; i++){
        freq[nums[i]]++;
    }
    let hold = 0;
    for(let i = 0; i < freq.length; i++){
        for(let j = 0; j < freq[i]; j++){
            nums[hold] = i;
            hold++;
        }
    }
};