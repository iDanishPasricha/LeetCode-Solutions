# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return []
        ans=[];
        stack = [(root,"")]
        
        while stack:
            node,string = stack.pop();
            if not node.left and not node.right:
                ans.append(string+str(node.val))
                
            if node.left:
                stack.append((node.left,string+str(node.val)+"->"))
            if node.right:
                stack.append((node.right,string+str(node.val)+"->"))
        final_list = [i.split("->") for i in ans]
        final_list = [[int(float(j)) for j in i] for i in final_list]
        for i in final_list:
            if sum(i)==targetSum:
                return True
        return False