/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    let b = new Set();
    let l = 0;
    for(let i = 0; i < nums.length; i++){
        if(i - l  > k){
            b.delete(nums[l]);
            l += 1;
        }
        if (b.has(nums[i])){
            return true;
        }
        b.add(nums[i])

        }

    
    return false;
};
