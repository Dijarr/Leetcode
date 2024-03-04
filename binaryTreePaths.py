# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
       res = []
       cur = []
       self.dfs(res, cur, root)
       return res

    def dfs(self, res, cur, node):
        if not node.right and not node.left:
            cur.append(str(node.val))
            res.append("->".join(cur[:]))
            cur.pop()
            return
        
        if node.right:
            cur.append(str(node.val))
            self.dfs(res, cur, node.right)
            cur.pop()

        if node.left:
            self.dfs(res, cur+[str(node.val)], node.left)