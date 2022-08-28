class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = Counter(s)
        stack = []
        visited = set()
        for i in s:
            if i not in visited:
                while stack and stack[-1]>i and d[stack[-1]]>0:
                    visited.remove(stack.pop())
                stack.append(i)
                visited.add(i)
            d[i]-=1
        return ''.join(stack)
                
    
    
    #while loop conditions --stack jinda hai na empty ta nhi   --lexicographical order maintained hai {a,b,c,d,e aivein like dictionary}  --d[digit] mukk te nhi gya kitte halle agge v aana hai na ,last occurence ta nhi c ehdi