# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # This list will store our final result values
        
        def helper(node):
            # Base case: If the node is empty (None), stop and return
            if not node:
                return
            
            # 1. Traverse the left subtree
            helper(node.left)
            
            # 2. Visit the current node (add its value to our list)
            res.append(node.val)
            
            # 3. Traverse the right subtree
            helper(node.right)
            
        # Kick off the helper function starting from the root
        helper(root)
        
        return res