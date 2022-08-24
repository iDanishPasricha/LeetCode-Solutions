class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            # space required for the needle to fit in 
            if haystack[i:i+len(needle)] == needle:
                return i
    
        return -1
        
        # ASK THE INTERVIEWER:-
        #What should we return when needle is an empty string?
'''
        ANOTHER APPROACH
        if not needle: return 0
        if needle not in haystack: return -1
        else:
            return haystack.index(needle)
    
        
        
                
haystack = "danishandtanuj"   len(haystack) = 14
needle   = "isha"             len(needle)   =  4
'''


