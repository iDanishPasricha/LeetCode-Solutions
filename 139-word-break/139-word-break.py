
class Solution:
    def wordBreak(self, s: str, d: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True
        
        for i in range(len(s),-1,-1):
            for word in d:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    dp[i] = dp[i+len(word)]
                if dp[i]: break
        return dp[0]
    
'''
just explain it with example s =  Catsanddog and wordDict = ["Cat","Cats","Sand","And","Dog"]

word_set = set(wordDict)
q = deque()
visited = set()
q.append(0)

while q:
    start = q.popleft()
    if start in visited:
        continue
    for end in range(start + 1, len(s) + 1):
        if s[start:end] in word_set:
            q.append(end)
            if end == len(s):
                return True
    visited.add(start)
return False


#Complexity
n is the length of the input string.

Time complexity : O(n^3) For every starting index, the search can continue till the end of the given string.

Space complexity : O(n). Queue of at most n size is needed.

'''