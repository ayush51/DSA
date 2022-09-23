class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return res
