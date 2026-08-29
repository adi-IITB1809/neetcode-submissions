# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        
        # Both are empty
        if not p and not q:
            return True

        # One is empty, or values are different
        if not p or not q or p.val != q.val:
            return False

        # Check left and right sides
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))