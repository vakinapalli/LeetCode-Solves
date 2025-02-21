/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let currow = new Array(n + 1).fill(0);
    let dummy = new Array(n + 1).fill(0);
    currow[currow.length - 1] = 1;
    for(let i = m - 1; i > -1; i--){
        for(let j = n - 1; j > -1; j--){
            currow[j] = currow[j + 1] + dummy[j];
        }
        let hold = dummy;
        dummy = currow;
        currow = hold.fill(0);
    }
    return dummy[0];
};