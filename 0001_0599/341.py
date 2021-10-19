# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: '[NestedInteger]'):
        self.stk = []
        def flatten(output, nl):
            if nl.isInteger():
                output.append(nl.getInteger())
            else:
                curr = nl.getList()
                while curr:
                    flatten(output, curr.pop(0))

        while nestedList:
            flatten(self.stk, nestedList.pop(0))

    def next(self) -> int:
        return self.stk.pop(0)


    def hasNext(self) -> bool:
        return self.stk != []


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# previous approach
# # """
# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# # """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> '[NestedInteger]':
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
#
# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         def flat(arr, nested):
#             while nested:
#                 t = nested[0]
#                 if t.isInteger():
#                     arr.append(t.getInteger())
#                 else:
#                     flat(arr, t.getList())
#                 nested = nested[1:]
#
#         self.stk = []
#         flat(self.stk, nestedList)
#
#     def next(self) -> int:
#         return self.stk.pop(0)
#
#     def hasNext(self) -> bool:
#         return True if self.stk else False
#
# # Your NestedIterator object will be instantiated and called as such:
# # i, v = NestedIterator(nestedList), []
# # while i.hasNext(): v.append(i.next())