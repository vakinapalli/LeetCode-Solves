class Solution {
public:
    bool doable(vector<int> piles, int h, int speed){
        int time = 0;
        for(int i = 0; i < piles.size(); i++){
            time += piles[i]/speed;
            if(piles[i] % speed > 0){
                time++;
            }
            if(time > h){
                return false;
            }
        }
        return true;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int a = 1;
        int b = *max_element(piles.begin(), piles.end());
        int m = 0;
        while(a <= b){
            m = (a + b)/2;
            if(doable(piles,h,m)){
                b = m - 1;
            }
            else{
                a = m + 1;
            }
        }
        return a;
    }
};