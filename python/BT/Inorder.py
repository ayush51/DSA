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
    
    
    Iterative:::::::::::::
                                                
                                                class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr!=None or stack:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
