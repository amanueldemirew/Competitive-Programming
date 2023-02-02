class MyCircularDeque:

    def __init__(self, k: int):
        self.cdq = []*k
        self.size = k

    def insertFront(self, value: int) -> bool:
        if len(self.cdq) < self.size:
            self.cdq.insert(0,value) 
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.cdq) < self.size:
            self.cdq.insert(self.size-1,value)
            return True
        
        return False

    def deleteFront(self) -> bool:
        if len(self.cdq) ==0:
            return False
        
        del self.cdq[0]
        return True

    def deleteLast(self) -> bool:
        if len(self.cdq) ==0:
            return False
        
        del self.cdq[-1] 
        return True
        
        del self.cdq[0]

    def getFront(self) -> int:
        if len(self.cdq) ==0:
            return -1
        
        return self.cdq[0]
        
    def getRear(self) -> int:
        if len(self.cdq) ==0:
            return -1
        
        return self.cdq[-1]
        

    def isEmpty(self) -> bool:
        return len(self.cdq) <= 0

    def isFull(self) -> bool:
        return len(self.cdq) == self.size
           
        
       
    
    


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()