/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    let tree = [];
    if(root == null){
        return tree;
    }
    let deque = [];
    deque.push(root);

    while(deque.length > 0){
        let h = [];
        let a = deque.length;
        for(let i = 0; i < a; i++){
            let temp = deque.shift();
            h.push(temp.val);
            if(temp.left != null){
                deque.push(temp.left);
            }
            if(temp.right != null){
                deque.push(temp.right);
            }
        }
        tree.push(h);
    }
    return tree;
};