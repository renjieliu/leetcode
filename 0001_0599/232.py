class MyQueue:

    def __init__(self): 
        self.stk = []
        

    def push(self, x: int) -> None: # O( 1 | 1 )
        self.stk.append(x)
        

    def pop(self) -> int: # O( 1 | 1 )
        return self.stk.pop(0)
        

    def peek(self) -> int:  # O( 1 | 1 )
        return self.stk[0]

    def empty(self) -> bool: # O( 1 | 1 )
        return self.stk == []
    
    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



