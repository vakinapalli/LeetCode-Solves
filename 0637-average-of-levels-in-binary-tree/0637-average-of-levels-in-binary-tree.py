# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = [0] * 10000
        self.lvlct = [0] * 10000
        self.lv = 0

    def trav(self, lvl, node):
        self.lv = max(self.lv, lvl )
        self.ans[lvl] += node.val
        self.lvlct[lvl] += 1
        if node.left:
            self.trav( lvl + 1, node.left)
        if node.right:
            self.trav( lvl + 1, node.right)
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        self.trav(0, root)
        fin = []
        for i in range(self.lv + 1):
            stu = float(self.ans[i])/self.lvlct[i]
            fin.append(stu)
        return fin

        
