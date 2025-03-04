class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        map<int, int> freq;
        int a = 0;
        int k = 0;
        for(int i = 0; i < nums.size(); i++){
            if(freq[nums[i]] >= 2){
                continue;
            }
            freq[nums[i]]++;
            nums[a] = nums[i];
            a++;
            k++;

        }
        return k;
    }
};