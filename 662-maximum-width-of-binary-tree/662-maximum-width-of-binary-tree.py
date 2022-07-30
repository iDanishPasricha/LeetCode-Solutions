# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        Q = collections.deque()
        Q.append((root,0))
        ans = 0
        while Q:                   # suppose ar some point
            _, start = Q[0]        #[(6,0) , (7,6) , (11,9) , (15,12)]
                                   #    start=0                    index=12   ans=index-start+1  = 13
            for i in range(len(Q)):
                node, index = Q.popleft()
                if node.left:
                    Q.append((node.left, 2*index))
                if node.right:
                    Q.append((node.right, 2*index+1))
            ans = max(ans, index-start+1)
        return ans
    
    
    