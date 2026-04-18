# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has depth 0
        if not root:
            return 0
        
        # Recursively find the depth of left and right subtrees
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # The depth of the current node is 1 + the max of its children
        return 1 + max(left_height, right_height)