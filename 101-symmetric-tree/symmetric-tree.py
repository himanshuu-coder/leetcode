# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # If both are None, they mirror each other
        if not t1 and not t2:
            return True
        # If only one is None, or values don't match, not a mirror
        if not t1 or not t2 or t1.val != t2.val:
            return False
        
        # Check cross-wise: (Left of T1 with Right of T2) AND (Right of T1 with Left of T2)
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)