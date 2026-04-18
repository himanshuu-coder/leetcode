# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1. Base case: If the tree is empty
        if not root:
            return False
        
        # 2. Check if we are at a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 3. Recursively check subtrees with the updated targetSum
        remaining_sum = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))