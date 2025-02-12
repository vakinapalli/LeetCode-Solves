# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        a = targetSum - root.val
        
        if not root.left and not root.right:
            if a == 0:
                return True
            else:
                 return False
        b = False
        c = False
        if root.left:
          b =  self.hasPathSum(root.left, a)
        if root.right:
           c = self.hasPathSum(root.right, a)
        return b or c
        