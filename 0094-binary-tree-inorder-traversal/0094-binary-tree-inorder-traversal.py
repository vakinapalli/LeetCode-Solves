# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def traverse(self, root, l):
        if not root:
            return
        self.traverse(root.left, l)
        l.append(root.val)
        self.traverse(root.right, l)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        hold = []    
        self.traverse(root, hold)
        return hold