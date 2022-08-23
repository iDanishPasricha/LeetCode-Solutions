class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        for value, symbol in digits:
            if num == 0: break # We don't want to continue looping if we're done.
            count = num//value
            num = num%value
            
            roman_digits.append(symbol * count) # Append "count" copies of "symbol" to roman_digits.
        return "".join(roman_digits)        
        
'''
num = 1994
and explain
'''
        
        
        
'''
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        ans = ''
        for i in d:
            while num >= i:
                ans += d[i]
                print(ans)
                num -= i
        return ans
'''