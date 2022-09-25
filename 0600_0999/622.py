class MyCircularQueue:

    def __init__(self, k: int):
        self.total = k
        self.arr = []


    def enQueue(self, value: int) -> bool: # O( 1 | 1 )
        if len(self.arr) == self.total:
            return False
        else:
            self.arr.append(value)
            return True

    def deQueue(self) -> bool: # O( 1 | 1 )
        if self.arr == []:
            return False
        else:
            self.arr.pop(0)
            return True

    def Front(self) -> int: # O( 1 | 1 )
        return self.arr[0] if self.arr else -1

    def Rear(self) -> int: # O( 1 | 1 )
        return self.arr[-1] if self.arr else -1
        

    def isEmpty(self) -> bool: # O( 1 | 1 )
        return self.arr == []
        

    def isFull(self) -> bool: # O( 1 | 1 )
        return len(self.arr) == self.total


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


# previous solution

# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.length = k
#         self.stk = []

#     def enQueue(self, value: int) -> bool:
#         if len(self.stk) >= self.length:
#             return False
#         else:
#             self.stk.append(value)
#             return True

#     def deQueue(self) -> bool:
#         if self.stk and self.stk:
#             self.stk.pop(0)
#             return True
#         else:
#             return False

#     def Front(self) -> int:
#         if self.stk:
#             return self.stk[0]
#         else:
#             return -1

#     def Rear(self) -> int:
#         if self.stk:
#             return self.stk[-1]
#         else:
#             return -1

#     def isEmpty(self) -> bool:
#         return self.stk == []

#     def isFull(self) -> bool:
#         return len(self.stk) == self.length

# # Your MyCircularQueue object will be instantiated and called as such:
# # obj = MyCircularQueue(k)
# # param_1 = obj.enQueue(value)
# # param_2 = obj.deQueue()
# # param_3 = obj.Front()
# # param_4 = obj.Rear()
# # param_5 = obj.isEmpty()
# # param_6 = obj.isFull()






