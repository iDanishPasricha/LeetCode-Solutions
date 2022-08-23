class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c = 0
        if len(s)==1: return False
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack:
                    if i==']' and stack[-1]=='[':
                        c+=2
                        stack.pop()
                    if i==')' and stack[-1]=='(':
                        c+=2
                        stack.pop()
                    if i=='}' and stack[-1]=='{':
                        c+=2
                        stack.pop()
        return c==len(s)                
    

            
            