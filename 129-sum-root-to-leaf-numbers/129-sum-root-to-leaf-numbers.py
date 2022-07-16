# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root," ")]
        ans=[];
        while stack:
            node,string = stack.pop(0)
            if node.right:
                stack.append((node.right,string+str(node.val)))
            if node.left:
                stack.append((node.left,string+str(node.val)))
            if not node.right and not node.left:
                ans.append(string+str(node.val))
        sum1=0;
        for i in ans:
            sum1+=int(i);
        return sum1