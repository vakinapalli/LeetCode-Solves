class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[] currow = new int[obstacleGrid[0].length + 1];
        int[] dummy  = new int[obstacleGrid[0].length + 1];
        currow[n] = 1;
        for(int i = m - 1; i > -1; i--){
            for(int j = n-1; j > -1; j--){
                if(obstacleGrid[i][j] == 1){
                    currow[j] = 0;
                }
                else{
                    currow[j] = currow[j + 1] + dummy[j];
                }
            }
            dummy = currow;
            currow = new int[n + 1];
        }
        return dummy[0];
    }
}