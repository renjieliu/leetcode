class MyHashMap: #O(N | N)

    def __init__(self):
        self.arr = [None for _ in range(10**6+1)]
        

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value
        

    def get(self, key: int) -> int:
        return self.arr[key] if self.arr[key] != None else -1
        

    def remove(self, key: int) -> None:
        self.arr[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



# previous solution

# class MyHashMap:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stk = []

#     def put(self, key: int, value: int) -> None:
#         """
#         value will always be non-negative.
#         """
#         if key >= len(self.stk):
#             self.stk += [-1] * (key - len(self.stk) + 1)
#         self.stk[key] = value

#     def get(self, key: int) -> int:
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         if key >= len(self.stk):
#             return -1
#         return self.stk[key]

#     def remove(self, key: int) -> None:
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         if key < len(self.stk):
#             self.stk[key] = -1

# # Your MyHashMap object will be instantiated and called as such:
# # obj = MyHashMap()
# # obj.put(key,value)
# # param_2 = obj.get(key)
# # obj.remove(key)


