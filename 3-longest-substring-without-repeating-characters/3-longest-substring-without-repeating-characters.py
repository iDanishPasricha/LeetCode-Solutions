class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0;
        temp_end=0;
        max_len=0;
        d={}
        while(temp_end<len(s)):
            
            if s[temp_end] in d and d[s[temp_end]]>=start:
                start=d[s[temp_end]]+1;
                
            max_len=max(max_len,temp_end-start+1);
            d[s[temp_end]]=temp_end;
            temp_end+=1;
            
        return max_len
                
        
        
            
