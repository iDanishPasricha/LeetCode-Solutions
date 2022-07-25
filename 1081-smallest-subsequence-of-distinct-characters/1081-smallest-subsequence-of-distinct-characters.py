class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1;
            else:
                d[s[i]]+=1;
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                while(stack and stack[-1]>s[i] and d[stack[-1]]>0):
                    temp = stack.pop()
                    visited.remove(temp)
                stack.append(s[i])
                visited.add(s[i])
            d[s[i]]-=1
            
                
        return ''.join(stack)
        