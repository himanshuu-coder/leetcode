# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return 0
            
            # Check the left subtree
            left_h = check_height(node.left)
            if left_h == -1:
                return -1
            
            # Check the right subtree
            right_h = check_height(node.right)
            if right_h == -1:
                return -1
            
            # If the difference is > 1, this node is unbalanced
            if abs(left_h - right_h) > 1:
                return -1
            
            # Otherwise, return the height of this node
            return 1 + max(left_h, right_h)
        
        # If the helper returns -1, the tree is unbalanced
        return check_height(root) != -1