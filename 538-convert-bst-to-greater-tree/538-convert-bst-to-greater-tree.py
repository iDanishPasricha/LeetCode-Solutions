# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sums = 0
        def inorder_reverse(root):
            if not root: return 
            inorder_reverse(root.right)
            self.sums+=root.val
            root.val = self.sums
            inorder_reverse(root.left)
            return root
            
            
        
        inorder_reverse(root)
        return root
        