class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()
        
        l = 0
        r = len(products)-1
        
        for i in range(len(searchWord)):
            c = searchWord[i]
            
            while l<=r and (len(products[l])<=i or products[l][i]!=c):
                l+=1
            while l<=r and (len(products[r])<=i or products[r][i]!=c):
                r-=1
            
            ans.append([])
            remain = r-l+1
            for j in range(min(3,remain)):
                ans[-1].append(products[l+j])
        return ans
        
        #O(nlogn) + n.w + m 
        
        #sorting + 2pointers (in worst case we have to iterate through every single word w) + m(we have to iterate through the impur searchWord)
        