# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)           # LEFT
            dfs(root.right)          # RIGHT
            result.append(root.val)  # ROOT

        dfs(root)
        return result