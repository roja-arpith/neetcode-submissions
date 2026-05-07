# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.count = 0

        def dfs(root, max_val):
            
            if not root:
                return 
                
            max_val = max(max_val,root.val)

            if max_val == root.val:
                self.count += 1
            
            dfs(root.left, max_val)
            dfs(root.right, max_val)

            return

        dfs(root,root.val)

        return self.count