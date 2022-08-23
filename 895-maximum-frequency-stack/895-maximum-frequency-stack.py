class FreqStack:

    def __init__(self):
        self.d={}
        self.max_frequency = 0
        self.stacks = {}
        

    def push(self, val: int) -> None:
        if val in self.d:
            frequency = 1 + self.d[val]
        else:
            frequency = 1
        
        self.d[val] = frequency
        
        if frequency > self.max_frequency:
            self.max_frequency = frequency
            self.stacks[frequency] = []
        self.stacks[frequency].append(val)
        

    def pop(self) -> int:
        ans = self.stacks[self.max_frequency].pop()
        self.d[ans]-=1;
        if not self.stacks[self.max_frequency]:
            self.max_frequency-=1;
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()