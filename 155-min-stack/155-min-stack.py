class MinStack:
    def __init__(self):

        self.stack= []

    def push(self, x):

        if not self.stack:
            self.stack.append((x,x)) 
        else:
            self.stack.append((x,min(x,self.stack[-1][1])))

    def pop(self):

        if self.stack: self.stack.pop()

    def top(self):

        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self):

        if self.stack: return self.stack[-1][1]
        else: return None


'''
[-3,-3]  min(-3,-2) = min(current number,previous minimum) = (x,min(x,self.stack[-1][1])
[0,-2]
[-2,-2]
'''