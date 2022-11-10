# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: 'List[NestedInteger]') -> int: # O( N | 1 )
        def helper(lst, lvl): 
            total = 0
            if lst:
                for curr in lst: # go through each element of the lst, and calulate the weighted sum
                    if curr.isInteger():
                        total += lvl * curr.getInteger()
                    else:
                        total += helper(curr.getList(), lvl+1)
            return total
        
        return helper(nestedList, 1) # default level is 1


                    
      
   
        



# previous solution

# # """
# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# # """
# #class NestedInteger:
# #    def __init__(self, value=None):
# #        """
# #        If value is not specified, initializes an empty list.
# #        Otherwise initializes a single integer equal to value.
# #        """
# #
# #    def isInteger(self):
# #        """
# #        @return True if this NestedInteger holds a single integer, rather than a nested list.
# #        :rtype bool
# #        """
# #
# #    def add(self, elem):
# #        """
# #        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
# #        :rtype void
# #        """
# #
# #    def setInteger(self, value):
# #        """
# #        Set this NestedInteger to hold a single integer equal to value.
# #        :rtype void
# #        """
# #
# #    def getInteger(self):
# #        """
# #        @return the single integer that this NestedInteger holds, if it holds a single integer
# #        Return None if this NestedInteger holds a nested list
# #        :rtype int
# #        """
# #
# #    def getList(self):
# #        """
# #        @return the nested list that this NestedInteger holds, if it holds a nested list
# #        Return None if this NestedInteger holds a single integer
# #        :rtype List[NestedInteger]
# #        """

# class Solution:
#     def depthSum(self, nestedList: 'List[NestedInteger]') -> int: # O( N | 1 )
#         def helper(output, lvl, lst): 
#             if lst:
#                 for curr in lst: # go through each element of the lst, and calulate the weighted sum
#                     if curr.isInteger():
#                         output[0] += lvl * curr.getInteger()
#                     else:
#                         helper(output, lvl+1, curr.getList())
#         output = [0] 
#         helper(output, 1, nestedList) # default level is 1
#         return output[0]


                    
      
   
        
        


# previous solution

# # """
# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# # """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """

#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """

#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """

#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """

#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """

#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# class Solution:
#     def depthSum(self, nestedList: 'List[NestedInteger]') -> int:
#         def helper(lst, depth):
#             output = 0
#             for i in range(len(lst)):
#                 curr = lst[i]
#                 if curr.isInteger():
#                     output += depth * curr.getInteger()
#                 else:
#                     output += helper(curr.getList(), depth+1)
#             return output

#         return helper(nestedList, 1)




