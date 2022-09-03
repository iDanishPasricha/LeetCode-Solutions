class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0;
        right = 0;
        maxLen = 0;
        
        while(right < len(s)):

            while(len(set(s[left:right+1]))!= len(s[left:right+1])):
                  left+=1;
            maxLen = max(maxLen , right-left+1);
            right+=1;
        return maxLen
    
    
    
    
# Time complexity : O(2n)=O(n). In the worst case each character will be visited twice by i and j.

# same complextity = same as brute foce O(min(m,n))

    
    ''' 
    Brute force
    Intuition

Check all the substring one by one to see if it has no duplicate character.

Time complexity : O(n^3)


Space complexity : O(min(n,m)). We need O(k) space for checking a substring has no duplicate characters, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
'''

        
        