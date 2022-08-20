class Solution:
    def fib(self, n: int,search={}) -> int:
        if n ==0 or n==1:
             return n
        if n not in search:
            search[n] = self.fib(n-1,search)+self.fib(n-2,search);
        return search[n]
    

        