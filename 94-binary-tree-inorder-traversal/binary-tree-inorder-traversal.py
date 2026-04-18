# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def helper(node):
            if not node:
                return
            
            # 1. Left
            helper(node.left)
            # 2. Root
            res.append(node.val)
            # 3. Right
            helper(node.right)
            
        helper(root)
        return res