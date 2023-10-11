#implementing styacks using queueus

class MyStack:

    def __init__(self):
        self.data=deque()
        

    def push(self, x: int) -> None:
        self.data.append(x)


    def pop(self) -> int:
       if(len(self.data)==0):
           return []
       if(len(self.data)==1):
            return self.data.popleft()
       for i in range(len(self.data)-1):
           self.push(self.data.popleft())   # pushes the first elements to the last so in order to get the last element the first and then we can return that value
       return self.data.popleft() 

    def top(self) -> int:
        return self.data[-1]
        

    def empty(self) -> bool:
        return len(self.data)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()