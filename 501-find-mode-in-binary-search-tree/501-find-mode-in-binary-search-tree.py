# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        q.append(root)
        ans=[]
        max1 = 0;
        d = collections.defaultdict(lambda: 0)
        while q:
            
            curr = q.popleft();
            
            d[curr.val] += 1
            if d[curr.val] > max1:
                max1 = d[curr.val]
                ans = [curr.val]
            elif d[curr.val] == max1:
                ans.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return ans

            
        
        
                
        