class MinStack:

    def __init__(self):
        self.stk = []
        self.minn = float('inf')
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.minn = min(self.minn, val)

    def pop(self) -> None:
        self.stk.pop()
        self.minn = min(self.stk) if self.stk else float('inf')

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# previous approach
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stk = []
#         self.minn = float('inf')
#         self.minStk = []

#     def push(self, x: int) -> None:
#         self.stk.append(x)
#         self.minn = min(self.minn, x)  # compare with current minumum when push to the stack
#         self.minStk.append(self.minn)

#     def pop(self) -> None:
#         self.stk.pop()
#         self.minStk.pop()
#         if self.minStk == []:
#             self.minn = float('inf')
#         else:
#             self.minn = self.minStk[-1]

#     def top(self) -> int:
#         return self.stk[-1]

#     def getMin(self) -> int:
#         return self.minStk[-1]

# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()