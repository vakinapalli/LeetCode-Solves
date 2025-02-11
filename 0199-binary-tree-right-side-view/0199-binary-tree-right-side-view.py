# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        if not root:
            return tree
        deques = deque()
        deques.append(root)
        while(len(deques) > 0):
            hold = deques[-1]
            for i in range(len(deques)):
                h = deques.popleft()
                if h.left:
                    deques.append(h.left)
                if h.right:
                    deques.append(h.right)

            tree.append(hold.val)
        return tree