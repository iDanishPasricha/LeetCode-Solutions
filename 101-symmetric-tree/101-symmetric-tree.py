class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val!=r.val:
                return False
            else:
                return helper(l.left,r.right) and helper(l.right,r.left)
            
        
        return helper(root,root)