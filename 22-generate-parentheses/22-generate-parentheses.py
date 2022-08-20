class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(temp , no_of_open_brackets,no_of_closed_brackets,ans,n):
            if len(temp)==2*n:
                ans.append(temp)
                return
            
            if no_of_open_brackets < n:
                helper(temp + "(" , no_of_open_brackets+1,no_of_closed_brackets,ans,n)
            
                
                
            if no_of_closed_brackets < no_of_open_brackets:
                helper(temp + ")", no_of_open_brackets,no_of_closed_brackets+1,ans,n)
            
            
            
            
        ans = []
        helper("",0,0,ans,n)
        return ans