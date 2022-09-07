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

            case1 = root.val
            case2 = root.val + max(ls,rs)
            case3 = root.val + ls + rs
            
            curr_ans = max(case1,case2,case3)
            ans      = max(curr_ans,ans)
            
            return max(case1,case2)
        '''
            temp = max(root.val + (max(ls,rs)),root.val) # max(case2,case3)
            curr_ans = max(temp,root.val+ls+rs) #max(temp,case1)
            ans = max(curr_ans,ans)
    

            return temp  # we are returning temp because in case 2 either we will pass through LS or RS if we return ans and suppose case 1 is maximum i.e (RD+LS+RS) is stored in ans variable ,then whole tree will be included and whole tree will be returned
        '''
        func(root);
        return ans
    
    #case 1:- rootdata>0 , LS>0 , RS>0 --> maxsum = RD+LS+RS
    #case 2:- (LS<0 , RS>0) or (LS>0 , RS<0) --> maxsum = RD + max(LS,RS)
    #case 3:- LS<0 and RS<0 --> maxsum = RD
    
        
        
                
            
        