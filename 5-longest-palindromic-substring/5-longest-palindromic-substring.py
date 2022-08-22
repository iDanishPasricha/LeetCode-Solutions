class Solution:
    def longestPalindrome(self, s: str) -> str:

        ongoing_max_length = 0
        for i in range(len(s)):
            
            l = i
            r = i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1) > ongoing_max_length:
                    ongoing_max_length = (r-l+1)
                    stored_string = s[l:r+1]
                l-=1;
                r+=1;
            
            l = i
            r = i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if (r-l+1) > ongoing_max_length:
                    ongoing_max_length = (r-l+1)
                    stored_string = s[l:r+1]
                l-=1;
                r+=1;
                
        return stored_string
    
    # O(n2)
    # a palindrome can be expanded from its center, and there are only 2n - 1 such centers. The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.
            
            
        
        
            
                
        
        