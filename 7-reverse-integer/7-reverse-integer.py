class Solution:
    def reverse(self, x: int) -> int:
        
        lower_limit = -2**31
        upper_limit =  2**31
        
        reversed_int = int(str(x)[::-1].replace("-",""))
                
        if (x>0 and x<upper_limit) and (reversed_int<=upper_limit):
            return reversed_int
        
        if (x<0 and x>lower_limit) and (reversed_int<=upper_limit-1):
            return -1*reversed_int
        else:
            return 0
        
