class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints)-k
        
        curr = sum(cardPoints[r:])
        
        ans = curr
        
        while r< len(cardPoints):
            curr+=(cardPoints[l] - cardPoints[r])
            ans = max(ans,curr)
            l+=1
            r+=1
            
        return ans
        