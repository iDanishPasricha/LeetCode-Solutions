class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        count = Counter(s)
        visited = set()
        stack = []

        for i in s:
            if i not in visited:  
                while stack and stack[-1] > i and count[stack[-1]] > 0:
                    print("stack before",stack)
                    visited.remove(stack.pop()) 
                    print("stack after",stack)
                stack.append(i)
                visited.add(i)
            count[i]-= 1
            
        return "".join(stack)
    
    
    #while loop conditions --stack jinda hai na empty ta nhi   --lexicographical order maintained hai {a,b,c,d,e aivein like dictionary}  --d[digit] mukk te nhi gya kitte halle agge v aana hai na ,last occurence ta nhi c ehdi