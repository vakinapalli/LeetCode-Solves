# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, h, k):
        if not root:
            return
        self.inorder(root.left,h, k)
        k[0] = k[0] - 1
        if k[0] == 0:
            h.append(root.val)
        self.inorder(root.right,h, k)
            

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        g = [k]
        self.inorder(root, h,g)
        return h[0]
