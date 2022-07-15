# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder[-1]);
        N=inorder.index(postorder[-1]);
        root.left=self.buildTree(inorder[:N],postorder[:N]);
        root.right=self.buildTree(inorder[N+1:],postorder[N:-1]);
        return root
        