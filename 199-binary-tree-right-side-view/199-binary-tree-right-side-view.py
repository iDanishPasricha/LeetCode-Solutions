# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        q=[]
        final_ans=[];
        q.append(root)
        ans=[];
        while(q):
            for i in range(len(q)):
                sub_ans=[];
            
                curr=q.pop(0);
                sub_ans.append(curr.val)
                if curr.left: q.append(curr.left);
                if curr.right: q.append(curr.right);
            
            ans.append(sub_ans)
        for i in ans:
            final_ans.append(i[-1]);
        return final_ans
        