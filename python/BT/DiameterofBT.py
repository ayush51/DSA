class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def diameter(root):
            if not root:
                return -1
            left = diameter(root.left)
            right = diameter(root.right)
            res[0] = max(res[0], left + right + 2)
            return 1 + max(left, right)
        
        diameter(root)
        return res[0]
        
