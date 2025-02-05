/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let a = 1;
    let b = n;
    let m = n;

    while(guess(m) != 0){
        m = Math.floor((a+b)/2);
        if(guess(m) == -1){
            b = m - 1;
        }
        else if(guess(m) == 1){
            a = m + 1;
        }
    }
    return m;
    
}