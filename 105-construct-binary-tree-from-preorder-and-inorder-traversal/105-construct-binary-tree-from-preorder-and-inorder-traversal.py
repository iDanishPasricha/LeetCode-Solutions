# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        
        
        root=TreeNode(preorder[0]);
        N=inorder.index(preorder[0]);
        root.left=self.buildTree(preorder[1:N+1],inorder[:N]);
        root.right=self.buildTree(preorder[N+1:],inorder[N+1:]);
        return root;
        