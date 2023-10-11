class MyQueue:

    def __init__(self):
        self.q=[]
        self.size=0
        

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size+=1

    def pop(self) -> int:
        if self.size==0: return "queue is empty"
        s=self.q.pop(0)
        self.size-=1
        return s

        

    def peek(self) -> int:
        if self.size==0: return "queue is empty"
        return self.q[0]
        

    def empty(self) -> bool:
        if self.size==0: return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()