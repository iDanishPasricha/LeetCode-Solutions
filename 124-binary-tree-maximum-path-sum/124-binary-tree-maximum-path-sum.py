# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")
        def func(root):
            nonlocal ans
            if root == None: return 0
            ls = func(root.left);
            rs = func(root.right);


            temp = max((max(ls,rs)+root.val),root.val)
            curr_ans = max(temp,root.val+ls+rs)
            ans = max(curr_ans,ans)

            return temp
        
        func(root);
        return ans
        
        
                
            
        