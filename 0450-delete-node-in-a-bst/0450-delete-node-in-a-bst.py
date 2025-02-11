from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # Case 1: Node has no children
            if not root.left and not root.right:
                return None
            # Case 2: Node has only right child
            elif not root.left:
                return root.right
            # Case 3: Node has only left child
            elif not root.right:
                return root.left
            # Case 4: Node has two children
            else:
                # Find inorder successor (smallest in right subtree)
                successor = self.findMin(root.right)
                root.val = successor.val
                # Recursively delete the inorder successor
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
