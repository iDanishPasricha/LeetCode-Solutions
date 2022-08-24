class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in  range(len(s)):
            last_index[s[i]] = i
        
        # we marked the last indices of each character in the string
        bookmark = 0
        ans = []
        temp = 0
        for i in range(len(s)):
            temp = max(temp,last_index[s[i]])
            if i==temp:
                ans.append(i+1 - bookmark)
                bookmark = i+1
        return ans

                
'''
Since each letter can appear only in one part, we cannot form a part shorter than the index of the last appearance of a letter subtracted by an index of the first appearance. For example here (absfab) the lengths of the first part are limited by the positions of the letter a. So it's important to know at what index each letter appears in the string last time. We can create a hash map and fill it with the last indexes for letters.
'''
            
'''
        Time: O(n) - 2 sweeps
Space: O(1) - hashmap consist of max 26 keys
'''