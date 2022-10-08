class MaxStack:

    def __init__(self):
        self.heap = []
        self.cnt = 0
        self.stack = []
        self.removed = set() #to track the removed index

    def push(self, x: int) -> None: # O( logN | N )
        heapq.heappush(self.heap, (-x, -self.cnt)) # add (-x, total cnt) into the heap
        self.stack.append((x, self.cnt))
        self.cnt += 1

    def pop(self) -> int: # O( logN | N )
        while self.stack and self.stack[-1][1] in self.removed: #update the heap, keep popping all the removed ones.
            self.stack.pop()
        num, idx = self.stack.pop()
        self.removed.add(idx)
        return num

    def top(self) -> int: # O( logN | N )
        while self.stack and self.stack[-1][1] in self.removed: #update the heap, keep popping all the removed ones.
            self.stack.pop()
        return self.stack[-1][0]
 
    def peekMax(self) -> int: # O( logN | N )
        while self.heap and -self.heap[0][1] in self.removed: #update the heap, keep popping all the removed ones.
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int: # O( logN | N )
        while self.heap and -self.heap[0][1] in self.removed: #update the heap, keep popping all the removed ones.
            heapq.heappop(self.heap)
        num, idx = heapq.heappop(self.heap)
        self.removed.add(-idx) #add current popped to the removed set
        return -num
    
    


# previous solution

# class MaxStack:

#     def __init__(self):
#         self.stk = []
        

#     def push(self, x: int) -> None:
#         self.stk.append(x)

#     def pop(self) -> int:
#         return self.stk.pop()

#     def top(self) -> int:
#         return self.stk[-1]

#     def peekMax(self) -> int:
#         return max(self.stk)

#     def popMax(self) -> int:
#         m = max(self.stk)
#         for i in range(len(self.stk)-1,-1,-1):
#             if self.stk[i] == m:
#                 self.stk = self.stk[:i] + self.stk[i+1:]
#                 break
#         # print(self.stk)
#         return m


# # Your MaxStack object will be instantiated and called as such:
# # obj = MaxStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.peekMax()
# # param_5 = obj.popMax()

