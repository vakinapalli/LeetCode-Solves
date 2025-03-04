class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        threshold = threshold * k;
        int a = 0;
        int sum = 0;
        int ct = 0;
        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
            if(i - a + 1 == k){
                if(sum >= threshold){
                    ct++;
                }
                sum -= arr[a];
                a+=1;
            }
            
        }
        return ct;
    }
}