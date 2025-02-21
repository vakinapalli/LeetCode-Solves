class Solution {
    public HashMap<Integer, Integer> memo = new HashMap<Integer, Integer>();

    public int climbStairs(int n) {
        if(n == 1 || n ==2){
            return n;
        }
        if(memo.get(n) != null){
            return memo.get(n);
        }
        memo.put(n, climbStairs(n - 1) + climbStairs(n-2));
        return memo.get(n);
    }
}