# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        if len(preorder) == 1:
            
            return TreeNode(preorder[0])
        root=TreeNode(postorder[-1]);
        n1=1;
        n2=preorder.index(postorder[-2]); 
        print(n2)
        
        root.left=self.constructFromPrePost(preorder[1:n2],postorder[:n2-1]);
        root.right=self.constructFromPrePost(preorder[n2:],postorder[n2-1:-1]);
        return root
        