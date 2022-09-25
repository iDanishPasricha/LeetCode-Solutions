class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        max_avg = 0
        
        def helper(node):
            nonlocal max_avg
            if not node:
                return 0, 0
            leftt, leftc = helper(node.left)
            rightt, rightc = helper(node.right)
            avg = (leftt+rightt+node.val)/(leftc+rightc+1)
            max_avg = max(max_avg, avg)
            return (leftt+rightt+node.val), (leftc+rightc+1)
        
        helper(root)
        
        return max_avg
    
    
    
    