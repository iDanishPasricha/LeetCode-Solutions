class MinStack:
    def __init__(self):

        self.stack= []
        self.minstack = []

    def push(self, val):
        self.stack.append(val);
        minstack_entry = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(minstack_entry) 

    def pop(self):

        self.stack.pop()
        self.minstack.pop()
        

    def top(self):

        return self.stack[-1]
        

    def getMin(self):

        return self.minstack[-1]


'''
[-3,-3]  min(-3,-2) = min(current number,previous minimum) = (x,min(x,self.stack[-1][1])
[0,-2]
[-2,-2]
'''