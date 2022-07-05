# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None: return
        
        elif root.val==p.val or root.val==q.val: return root
    
        elif p.val>root.val and q.val>root.val: return self.lowestCommonAncestor(root.right,p,q);  #dovein right side te ne
        
        elif p.val<root.val and q.val<root.val: return self.lowestCommonAncestor(root.left,p,q);   #dovein left side te ne
        
        elif p.val<root.val and q.val>root.val or q.val<root.val and p.val>root.val: return root  #ik left te ik right side te aa.
        