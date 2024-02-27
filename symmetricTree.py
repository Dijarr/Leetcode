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
        return self.helper(root.left, root.right)

    def helper(self, lst, rst):
        if not lst and not rst:
            return True
        if not lst or not rst:
            return False
        if lst.val != rst.val:
            return False
        return self.helper(lst.left, rst.right) and self.helper(lst.right, rst.left)