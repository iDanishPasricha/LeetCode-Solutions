# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        
        #remember if we are starting at a node we can only split once because if we violate this condition them it will no longer be a path
        
        
        #return sum with considering no split allowed 
        def dfs(root):
            if not root: return 0
            
            leftMax  = dfs(root.left)
            rightMax = dfs(root.right)
            
            leftMax  = max(leftMax,0)  #handling negative cases if leftmax is -ve then wont take it
            rightMax = max(rightMax,0) #handling negative cases if rigtmax is -ve then wont take it
            
            #compute maxSum WITH split (split allowed we can go in both directions left and right from root)
            
            ans[0] = max(ans[0] , leftMax + rightMax + root.val)
            
            return root.val + max(leftMax,rightMax)
            
            
        '''
A node can only appear in the sequence at most once. 
we are returning max(case1,case2) because in case 2 either we will pass through LS or RS if we return ans and suppose case 1 is maximum i.e (RD+LS+RS) is stored in ans variable ,then whole tree will be included and whole tree will be returned
        '''
        dfs(root);
        return ans[0]
    
    #case 1:- rootdata>0 , LS>0 , RS>0 --> maxsum = RD+LS+RS
    #case 2:- (LS<0 , RS>0) or (LS>0 , RS<0) --> maxsum = RD + max(LS,RS)
    #case 3:- LS<0 and RS<0 --> maxsum = RD
    
        
        
                
            
        