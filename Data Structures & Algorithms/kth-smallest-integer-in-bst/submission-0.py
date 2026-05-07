# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        queue = deque([root])
        res = []

        while queue:
            length = len(queue)

            for i in range(length):
                node = queue.popleft()

                res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        heapq.heapify(res)

        while k > 1:
            heapq.heappop(res)
            k -= 1
        
        return res[0]
