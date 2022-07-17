class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g);
        s = sorted(s);
        print(g)
        print(s)
        count=0;
        for i in range(len(g)):
            bhukh = g[i];
            for j in range(len(s)):
                if bhukh<=s[j]:
                    count+=1;
                    s.remove(s[j]);
                    break
        return count
    
            
            
        