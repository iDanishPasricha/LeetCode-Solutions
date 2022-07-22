class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]]=i;
        print(last_index)
        bookmark = 0;
        temp = 0
        ans = [];
        for i in range(len(s)):
            temp = max(temp,last_index[s[i]])
            if i==temp:
                ans.append(i+1-bookmark)
                bookmark = i+1;
        return ans
                
                
            
        
        