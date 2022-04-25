# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator): #O(N | N)
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.arr = []
        while True:
            self.arr.append(iterator.next()) 
            if not iterator.hasNext():
                break
        

    def peek(self): #O(1 | 1)
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.arr[0]
        

    def next(self): #O(1 | 1)
        """
        :rtype: int
        """
        return self.arr.pop(0)
        

    def hasNext(self): #O(1 | 1)
        """
        :rtype: bool
        """
        return self.arr != []
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].




# previous solution

# # Below is the interface for Iterator, which is already defined for you.
# #
# # class Iterator:
# #     def __init__(self, nums):
# #         """
# #         Initializes an iterator object to the beginning of a list.
# #         :type nums: List[int]
# #         """
# #
# #     def hasNext(self):
# #         """
# #         Returns true if the iteration has more elements.
# #         :rtype: bool
# #         """
# #
# #     def next(self):
# #         """
# #         Returns the next element in the iteration.
# #         :rtype: int
# #         """

# class PeekingIterator:
#     def __init__(self, iterator):
#         """
#         Initialize your data structure here.
#         :type iterator: Iterator
#         """
#         self.stk = [] 
#         while iterator.hasNext():
#             self.stk.append(iterator.next())       
        
#     def peek(self):
#         """
#         Returns the next element in the iteration without advancing the iterator.
#         :rtype: int
#         """
#         if self.stk:
#             return self.stk[0]
        

#     def next(self):
#         """
#         :rtype: int
#         """
#         if self.stk:
#             return self.stk.pop(0)
        

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return len(self.stk) > 0
        

# # Your PeekingIterator object will be instantiated and called as such:
# # iter = PeekingIterator(Iterator(nums))
# # while iter.hasNext():
# #     val = iter.peek()   # Get the next element but not advance the iterator.
# #     iter.next()         # Should return the same value as [val].



