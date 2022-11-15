# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        
        count = 0
        
        while q:
            node = q.popleft()
            
            if node:
                count += 1
                q.append(node.left)
                q.append(node.right)
        return count
                
        
        
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
