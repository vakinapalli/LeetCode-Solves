class Solution {

    public void color(int row, int col, int maxi, int maxj, char[][] grid){
        if(row < 0 || col < 0 || row == maxi || col == maxj){
            return;
        }
        if(grid[row][col] == '1'){
            grid[row][col] = '2';
            color(row - 1, col, maxi, maxj, grid);
            color(row + 1, col, maxi, maxj, grid);
            color(row, col - 1, maxi, maxj, grid);
            color(row, col + 1, maxi, maxj, grid);
        }

    }
    public int numIslands(char[][] grid) {
        int ct = 0;
        int maxheight = grid.length;
        int maxlength = grid[0].length;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    ct += 1;
                    color(i,j,maxheight,maxlength, grid);
                }
            }
        }
        return ct;
    }
}