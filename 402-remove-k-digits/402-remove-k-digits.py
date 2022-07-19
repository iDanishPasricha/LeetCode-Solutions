class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        if len(nums)==1: return "0"
        stack = [];
        for i in nums:
            while(k>0 and stack and stack[-1]>i):
                stack.pop();
                k-=1;
            stack.append(i);
        while k>0 and stack:
            stack.pop();
            k-=1
        return "".join(stack).lstrip("0") or "0"


        