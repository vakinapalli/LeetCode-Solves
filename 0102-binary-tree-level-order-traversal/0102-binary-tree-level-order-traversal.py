# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = []
        if not root:
            return tree
        queue = deque()
        queue.append(root)
        while(len(queue) > 0):
            hold = []
            for i in range(len(queue)):
                h = queue.popleft()
                hold.append(h.val)
                if h.left:
                    queue.append(h.left)
                if h.right:
                    queue.append(h.right)
            tree.append(hold)
        return tree
