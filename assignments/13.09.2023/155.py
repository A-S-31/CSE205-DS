class MinStack(object):

    def __init__(self):
        self.data=[]
        

    def push(self, val):
        self.data.append(val)
        

    def pop(self):
        if(len(self.data)==0):
            return "Stack is empty"
        return self.data.pop()

    def top(self):
        if(len(self.data)==0):  
            return "Stack is empty"
        return self.data[-1]


    def getMin(self):
        if(len(self.data)==0):
            return "Stack is empty"
        return min(self.data)
    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()