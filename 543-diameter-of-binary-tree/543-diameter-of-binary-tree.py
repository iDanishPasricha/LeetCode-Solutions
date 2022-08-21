class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root):
            nonlocal diameter
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
        
        diameter = 0
        height(root)
        return diameter
    
    
    '''
    class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxPath(root):
            nonlocal maxSum
            if not root:
                return 0
            
            left = maxPath(root.left)
            right = maxPath(root.right)
            maxSum = max(maxSum, left + right + root.val)
            return max(left + root.val, right + root.val, 0)
        
        maxSum = -math.inf  
        maxPath(root)
        return maxSum
    '''
        
        