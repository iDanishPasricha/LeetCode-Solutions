class Solution(object):
    def romanToInt(self, s):

        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        x=0
        
        for i in s:
            x+=d[i]
        print(x)
        
        
        if 'IV' in s or 'IX' in s: x-=2 #because see I + V = 1+5 = 6 ,6 add kiye hai BUT ACTUAL 4 so -2
        if 'XL' in s or 'XC' in s: x-=20 #because see X + C = 10+100 = 110 ,110 add kiye hai BUT ACTUAL 90 so -20
        if 'CD' in s or 'CM' in s: x-=200 #because see C + M = 100+1000 = 1100 ,1100 add kiye hai BUT ACTUAL 900 so -200
        
        return x