class Solution {
public:
    void color(int i,int j,int& maxi,int& maxj,int& trck, vector<vector<int>>& grid){
        if(i < 0 || j < 0 || i == maxi || j == maxj){
            return; 
        }
        if(grid[i][j] == 1){
            grid[i][j] = 2;
            trck++;
            color(i + 1, j, maxi, maxj, trck, grid);
            color(i - 1, j, maxi, maxj, trck, grid);
            color(i, j - 1, maxi, maxj, trck, grid);
            color(i, j + 1, maxi, maxj, trck, grid);
            
        }
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxim = 0;
        int ck = 0;
        int im = grid.size();
        int jm = grid[0].size();
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[0].size(); j++){
                if(grid[i][j] == 1){
                    color(i,j,im, jm, ck, grid);
                    maxim = max(maxim, ck);
                    ck = 0;
                }
            }
        }
        return maxim;
        
    }
};