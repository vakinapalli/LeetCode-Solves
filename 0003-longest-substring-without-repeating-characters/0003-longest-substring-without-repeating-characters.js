/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let hold = new Set();
    let a = 0;
    let lnth = 0;
    for(let i = 0; i < s.length; i++){
        while(hold.has(s[i])){
            hold.delete(s[a]);
            a++;
        }
        hold.add(s[i]);
        lnth = Math.max(lnth, i-a+1);
    }
    return lnth;
};