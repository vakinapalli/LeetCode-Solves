class Solution {
    public int lastStoneWeight(int[] stones) {

        if(stones.length == 1){
            return stones[0];
        }
        PriorityQueue<Integer> p = new PriorityQueue<>();
        for(int i = 0; i < stones.length; i++){
            p.add( stones[i] * -1);
            
        }
        int a = 0;
        int b = 0;
         
        
        while(p.size() > 1){
            a = -1 * p.poll();
            b = -1 * p.poll();

            if(Math.abs(a - b) > 0){
                p.add(-1 * Math.abs(a-b));
            }
        }
        if(p.size() > 0){
            return -1 * p.peek();
        }
        return 0;


    }
}