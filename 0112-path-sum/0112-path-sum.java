/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null){
            return false;
        }
        int a = targetSum - root.val;

        if(root.left == null && root.right == null){
            if(a == 0){
                return true;
            }
            else{
                return false;
            }
        }
        boolean c = false;
        boolean d = false;

        if(root.left != null){
            c = hasPathSum(root.left, a);
        }
        
        if(root.right != null){
            d = hasPathSum(root.right, a);
        }

        return c || d;
    }
}