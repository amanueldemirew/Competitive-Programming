class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        elif self.minstack[-1] >= val:
            self.minstack.append(val)           
            
        

    def pop(self) -> None:
        x = self.stack.pop()
        if self.minstack[-1] == x:    
            self.minstack.pop()
        return x 
        

    def top(self) -> int:
        return self.stack[-1]       

    def getMin(self) -> int:
        if len(self.minstack)== 0:
            return 
        else:
            return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()