# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def binaryTreePaths(root):
            if not root: return []
            ans=[];
            stack = [(root,"")]

            while stack:
                node,string = stack.pop();
                if not node.left and not node.right:
                    ans.append(string+str(node.val))

                if node.left:
                    stack.append((node.left,string+str(node.val)+","))
                if node.right:
                    stack.append((node.right,string+str(node.val)+","))
            return ans
        
        
        ans = (binaryTreePaths(root))
        print(ans)
        final_ans = [];
        for i in range(len(ans)):
            sum1=0;
            ans[i] = [int(s) for s in ans[i].split(',')]
            for j in ans[i]:
                if j==",":continue;
                else:sum1+=j;
            if sum1==targetSum:
                final_ans.append(ans[i])
        return final_ans
        