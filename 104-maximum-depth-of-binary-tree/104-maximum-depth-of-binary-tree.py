# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q= deque();
        q.append(root);
        levels=0;
        if not root: return 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left);
                if curr.right:
                    q.append(curr.right);
            levels+=1;
        return levels
                
        