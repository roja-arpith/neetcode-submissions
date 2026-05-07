# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def dfs(min,max,root):
            if not root:
                return True
            
            if not (min < root.val < max):
                return False
            
            return dfs(min,root.val,root.left) and dfs(root.val,max,root.right)


        return dfs(float('-inf'),float('inf'),root)
         