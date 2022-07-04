class Solution:
    def reverseParentheses(self, s: str) -> str:
        
            
        stack = [];
        for i in range(len(s)):
            if s[i] == ')':
                temp="";
                while(stack and stack[-1]!='('):
                    curr = stack.pop();
                    temp+=str(curr)
                stack.pop()
                for j in temp:
                    stack.append(j);
            else:
                stack.append(s[i]);
        return ''.join(stack)
        
        