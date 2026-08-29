# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(root):
            if not root:
                return

            result.append(root.val)  # ROOT
            dfs(root.left)           # LEFT
            dfs(root.right)          # RIGHT

        dfs(root)
        return result