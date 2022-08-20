class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=[];
        left = right = 0;
        maxLen = 0;
        
        while(right<len(s)):

            if len(set(s[left:right+1])) < len(s[left:right+1]):
                while(len(set(s[left:right+1]))!=len(s[left:right+1])):
                    left+=1;
            maxLen = max(maxLen,right-left+1)
            right+=1
        return maxLen