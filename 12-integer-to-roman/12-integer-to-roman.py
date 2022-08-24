class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        for value, symbol in digits:
            if num == 0: break # We don't want to continue looping if we're done.
            count = num//value # how many times which we have to use a specific symbol
            num = num%value
            
            roman_digits.append(symbol * count) # Append "count" copies of "symbol" to roman_digits.
        return "".join(roman_digits)        
        
'''
num = 1994
and explain
        
Time complexity : O(1).

As there is a finite set of roman numerals, there is a hard upper limit on how many times the loop can iterate. This upper limit is 15 times, and it occurs for the number 3888. Therefore, we say the time complexity is constant, i.e. O(1).

Space complexity :O(1).

The amount of memory used does not change with the size of the input integer, and is therefore constant.


        
ANOTHER APPRAOCH
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        ans = ''
        for i in d:
            while num >= i:
                ans += d[i]
                num -= i
        return ans
'''