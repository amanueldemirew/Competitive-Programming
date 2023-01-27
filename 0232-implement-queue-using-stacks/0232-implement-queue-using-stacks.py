class MyQueue:

    def __init__(self):        
        self.queue = []       

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)       
        

    def peek(self) -> int:
        return self.queue[0]
        
        

    def empty(self) -> bool:
        if len(self.queue)== 0:
            return True            
        else:
            return False
            
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()