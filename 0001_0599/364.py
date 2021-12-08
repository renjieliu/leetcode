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
    def depthSumInverse(self, nestedList: 'List[NestedInteger]') -> int:
        arr = [] # [num, depth]
        def helper(arr, nested, depth): #to get all the numbers, along with the level
            for n in nested:
                if n.isInteger():
                    arr.append([n.getInteger(), depth])
                else:
                    helper(arr, n.getList(), depth+1)
        
        helper(arr, nestedList,1)
        maxLevel = 0 #find the maxLevel in the nestedList
        for a in arr:
            if a:
                maxLevel = max(maxLevel, a[1])
        output= 0 

        for n, level in arr: 
            output += n * (maxLevel-level+1)
        return output
    
 
        
        
        
        

        
        
        
        