class Vector2D:

    def __init__(self, vec: 'List[List[int]]'): #O( MN | MN )
        self.arr = [] 
        for r in vec: #flatten the 2D array
            for c in r:
                self.arr.append(c)
        
    def next(self) -> int: # get the first item
        return self.arr.pop(0)
    
    def hasNext(self) -> bool: #check if the array is empty
        return self.arr != []


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()




# previous solution

# class Vector2D:

#     def __init__(self, v: 'List[List[int]]'):
#         def flat(recr, stk):
#             while recr:
#                 curr = recr.pop(0)
#                 if isinstance(curr, list):
#                     if len(curr) > 0:
#                         flat(curr, stk)
#                 else:
#                     stk.append(curr)

#         recr = v.copy()
#         self.stk = []
#         while recr:
#             flat(recr.pop(0), self.stk)

#     def next(self) -> int:
#         return self.stk.pop(0)

#     def hasNext(self) -> bool:
#         return True if self.stk else False

# # Your Vector2D object will be instantiated and called as such:
# # obj = Vector2D(v)
# # param_1 = obj.next()
# # param_2 = obj.hasNext()


