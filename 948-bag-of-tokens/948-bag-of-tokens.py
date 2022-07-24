class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0;
        j = len(tokens)-1
        score = 0;
        while(i<=j):
        
            if power >= tokens[i]:
                power-=tokens[i]
                score+=1;
                i+=1
            else:
                if power + tokens[j]>=tokens[i] and i!=j and score!=0:
                    power+=tokens[j]
                    score-=1;
                    j-=1
                else:
                    break
        return score
    '''
Sort the tokens, l = 0 and r = length - 1
If there is enough power to flip the token[l], then do it and get 1 point.
if there is not enough power to flip token[l], then use 1 point to get the token[r] power.
If can not do both, stop.
'''